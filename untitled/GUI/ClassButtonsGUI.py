#Using Classes for creating GUI

from tkinter import *

class Application(Frame):
    #App with 3 buttons
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Creates 3 buttons
        # Button1 inside the Frame
        bttn1 = Button(self, text="Я ничего не делаю!")
        bttn1.grid()

        # Button2 inside the Frame
        bttn2 = Button(self)
        bttn2.grid()
        bttn2.configure(text="Я тоже!")

        # Button3 inside the Frame
        bttn3 = Button(self)
        bttn3.grid()
        bttn3["text"] = "И я тоже!"


root = Tk()
root.title("Бесполезные кнопки")
root.geometry("200x200")

app = Application(root)

root.mainloop()
