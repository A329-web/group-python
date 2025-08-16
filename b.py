from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","VIRUS detected!!!!")

b1 = Button(root,text="click me",command=msg)
b1.place(x=40,y=80)

def msg1():
    messagebox.showerror("Error", "Error detected!!!!")


b2 = Button(root, text="click me again", command=msg1)
b2.place(x=40, y=120)

def msg3():
    messagebox.showinfo("Info", "info detected!!!!")


b3 = Button(root, text="click me 3", command=msg3)
b3.place(x=40, y=160)


root.mainloop()