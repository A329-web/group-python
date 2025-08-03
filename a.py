from tkinter import *   #import 
from datetime import date
root = Tk()  #creating window
root.title("widgets")  #title of window
root.geometry('400x400')
root.configure(bg="lightblue")
l1 = Label(text="Hey!! There!!",fg="white",bg="grey",height=1,width=300)
l2 = Label(text="Full Name: ",bg="grey")
e1 = Entry()
def display():
    name = e1.get()
    global msg 
    msg = "Welcome to the application.\nToday's date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,msg)
    text_box.insert(END,date.today())

text_box = Text(height=3)
b1 = Button(text="Begin",command=display,height=1,bg="black",fg="white")

l1.pack()
l2.pack()
e1.pack()
b1.pack()
text_box.pack()
root.mainloop()







