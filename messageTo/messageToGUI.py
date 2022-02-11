from distutils.log import error
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from messageToGUI_ui import MessageToGUI
import csv
import requests
import json


class CustomMessageToGUI(MessageToGUI):
    pass

    def readRecipents(csvfile):
      with open(csvfile, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')

    def bRecipent_command(self, *args):
      fileTypes = (
        ('CSV', '*.csv'),
        ('All files', '*.*')
      )
      recipentsCSV = filedialog.askopenfilename(filetypes=fileTypes)
      with open(recipentsCSV, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        self.lbRecipents.delete(0, END)
        for row in reader:
          self.lbRecipents.insert(END, row)
      pass

    def bSend_command(self, *args):
      f = open("accesskeys", "r")
      PERSONAL_KEY = f.readline().strip()
      SYSTEM_KEY = f.readline().strip()
      WEB_KEY = f.readline().strip()
      requestCall = "https://www.divera247.com/api/users?accesskey=" + SYSTEM_KEY
      response = requests.get(requestCall)

      if response.status_code != 200:
        print("Fehler beim laden der Nutzerdaten aufgetreten.")
        exit()

      user = response.json()['data']

      user_ids = []
      missing_user = []
      for row in self.lbRecipents.get(0, END):
        searchresult = list(filter(lambda x:(x["lastname"] == row[0] and x["firstname"] == row[1]),user))
        if len(searchresult) == 0:
          print("cannot find " + row[0] + " " + row[1])
          missing_user.append(row)
        else :
          if len(searchresult) != 1:
            print("irgendwie sind hier zu viele Daten")
          else:
            user_ids.append(searchresult[0]['user_cluster_relation_id'])

      if missing_user.count != 0:
        missingUserMessage = "Folgende Helfer konnten in Divera nicht gefunden werden:\n"
        for user in missing_user:
          missingUserMessage = missingUserMessage + user[0] + " " + user[1] + "\n"
        messagebox.showwarning("Fehlende Divera Nutzer", missingUserMessage) 

      api_url = "https://www.divera247.com/api/v2/news"
      newMessage = {
        "News" : {
          "title" : self.eTitle.get(),
          "text"  : self.tMessage.get(1.0, "end-1c"),
          "send_push" : self.usePush.get(),
          "send_sms" : False,
          "send_call": False,
          "send_pager": False,
          "send_mail" : self.useMail.get(),
          "notification_type" : 4,
          #"user_cluster_relation" : user_ids,
        },
        "usingUserClusterRelations" : user_ids,
        "accesskey" : PERSONAL_KEY
      }
      print(json.dumps(newMessage))

      response = requests.post(api_url, json=newMessage)
      print(response.json())
      if response["success"] ==True:
        messagebox.showinfo("Erfolg!", "Nachricht wurde erfolgreich übermittelt.")
      else:
        errormessage = "Es ist folgender Fehler aufgetreten\n" + response['errors']
        messagebox.showerror("Fehler beim Senden", errormessage)
      pass

def main():
    root = Tk()
    ui = CustomMessageToGUI(root)
    root.title('MessageTo')
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
