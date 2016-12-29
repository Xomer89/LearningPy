#ClickCounting button

from tkinter import *

class Application(Frame):
    #App with 3 buttons
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Количество кликов: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """Increases the number of clicks"""
        self.bttn_clicks += 1
        self.bttn["text"] = "Количество кликов: " + str(self.bttn_clicks)

#Main part of the code
root = Tk()
root.title("Количество кликов")
root.geometry("200x50")
app = Application(root)
root.mainloop()
