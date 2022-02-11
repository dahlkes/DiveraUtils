import tkinter

class MessageToGUI(object):
    def __init__(self, root):
        self.lTitle = tkinter.Label(root,
            text = "Titel",
        )
        self.eTitle = tkinter.Entry(root,
            width = 0,
        )
        self.lMessage = tkinter.Label(root,
            text = "Nachricht",
        )
        self.tMessage = tkinter.Text(root,
            autoseparators = 0,
            height = 10,
            width = 0,
        )
        self.bRecipent = tkinter.Button(root,
            text = u"Empf\u00E4nger",
        )
        self.lbRecipents = tkinter.Listbox(root,
            width = 0,
        )
        self.usePush = tkinter.BooleanVar()
        self.useMail = tkinter.BooleanVar()
        self.cbPush = tkinter.Checkbutton(root,
            text = "Push",
            variable=self.usePush
        )
        self.cbMail = tkinter.Checkbutton(root,
            text = "E-Mail",
            variable=self.useMail
        )
        self.bSend = tkinter.Button(root,
            text = "Senden",
        )
        self.bRecipent.configure(
            command = self.bRecipent_command
        )
        self.bSend.configure(
            command = self.bSend_command,
        )

        # Geometry Management
        self.lTitle.grid(
            in_    = root,
            column = 1,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nw"
        )
        self.eTitle.grid(
            in_    = root,
            column = 2,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "ew"
        )
        self.lMessage.grid(
            in_    = root,
            column = 1,
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nw"
        )
        self.tMessage.grid(
            in_    = root,
            column = 2,
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self.bRecipent.grid(
            in_    = root,
            column = 1,
            row    = 3,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nw"
        )
        self.lbRecipents.grid(
            in_    = root,
            column = 2,
            row    = 3,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self.cbPush.grid(
            in_    = root,
            column = 1,
            row    = 4,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nw"
        )
        self.cbMail.grid(
            in_    = root,
            column = 2,
            row    = 4,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nw"
        )
        self.bSend.grid(
            in_    = root,
            column = 1,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "w"
        )


        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 18, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 128, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 83, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 25, pad = 0)
        root.grid_rowconfigure(5, weight = 0, minsize = 31, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 103, pad = 0)
        root.grid_columnconfigure(2, weight = 0, minsize = 170, pad = 0)


