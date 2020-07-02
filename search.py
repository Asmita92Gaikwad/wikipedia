import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

def quetion_answer():
    question = e1.get()
    answer = wikipedia.summary(question)
    showinfo("answer", answer)
    print(answer)

root = Tk()
root.geometry("400x400")

question = StringVar()
e1 = Entry(root,textvariable = question)
e1.grid(row = 1,column = 1)

b1 = Button(root,width = 12,command = quetion_answer)
b1.grid(row = 3,column =2)

root.mainloop()