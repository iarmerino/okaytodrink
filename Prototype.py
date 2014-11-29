import sys
from tkinter import *
def mhello():
    
    stext = ment.get()
    label2 = Label(root, text = 'Okay to Drink?', fg = 'blue').pack()
    return

def callback():
    print (ment.get())
root = Tk()
ment = StringVar()
def callback_2():
    print (ment.get())
    print (ment2.get())
ment2 = StringVar()

root.geometry('450x450')
root.title('Okay to Drink?')

label = Label(text = 'Okay to Drink?', fg = 'blue').pack()
entry = Entry(root, textvariable = ment).pack()


label2 = Label(text = 'Okay to Drink?', fg = 'blue').pack()
entry2 = Entry(root, textvariable = ment2).pack()
button2 = Button(text = 'OK', command = callback_2).pack()
root.mainloop()
