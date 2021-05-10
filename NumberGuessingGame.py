#Number Guessing Game 
from tkinter import *
from tkinter.messagebox import showinfo
import random

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        
        self.create_widgets()
        self.number = str(random.randrange(0,9))
        #Creates random number range between 1-9
    def create_widgets(self):
        self.lbl1 = Label(self, text = "Number Guessing Game")
        self.lbl1.grid(row = 0, column = 0)
        
        self.entry1 = Entry(self, width = 40)
        self.entry1.grid(row = 1, columnspan = 5, sticky =W)
        self.entry1.bind('<KeyPress>', self.enter)
        #Clicking enter key is the same as clicking the 'Guess' button
        self.bttn = Button(self, text= "Guess", command = self.number_guess)
        self.bttn.grid(row = 2, column = 2, sticky =W)
        
    def number_guess(self):
        print(self.number)
        if self.entry1.get() == self.number:
            showinfo(message = "Correct")
        #New seperate window pops up if guess is correct 
        else:
            self.entry1.delete(0, END)
            self.lbl1["text"] = "Try again!"
            
    def enter(self, event):
        if event.keysym == "Return":
            self.number_guess()
#main     
root = Tk()
root.title("Number Guessing Game")
root.geometry("500x500")
root.resizable(width = FALSE, height = FALSE)
app = Application(root)
root.mainloop()


