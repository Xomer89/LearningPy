#Program wich tells you the Secret of long life

from tkinter import *

class Application(Frame):
    """GUI"""
    def __init__(self, master):
        """Initializing the app frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creating button, text field and text region"""
        self.inst_lbl = Label(self, text="To discover the secret of longlivity enter password")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        #Password label
        self.pw_lbl=Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        #Text field
        self.pw_ent=Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        #Button for sending results
        self.submit_bttn=Button(self, text="Discover secret", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)

        #Text area for the secret
        self.secret_txt=Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """Different messages depending on the entered password"""
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "To live up to 100 years, you have to live up to 99, " \
            "and then be REALY carefull"
        else:
            message = "The password you entered is incorrect, " \
            "so I can't share the secret with you."

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


#main

root = Tk()
root.title("Highlander")
root.geometry("350x200")
app = Application(root)
root.mainloop()







