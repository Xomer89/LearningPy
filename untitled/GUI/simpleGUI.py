#Demonstrates a simple GUI

from tkinter import *

#Base window
root = Tk()

#Editing the window
root.title("Простейший GUI")
root.geometry("200x100")

#Frame
app = Frame(root)
app.grid()

#A Label inside the Frame
lbl = Label(app, text="Это я!")
lbl.grid()

#Button1 inside the Frame
bttn1 = Button(app, text="Я ничего не делаю!")
bttn1.grid()

#Button2 inside the Frame
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="Я тоже!")

#Button3 inside the Frame
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И я тоже!"


root.mainloop()