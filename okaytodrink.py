import sys
from tkinter import *

def keyPress(event):
    if event.char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print(event.char)
    elif event.keysym not in ('Alt_r', 'Alt_l', 'F4', 'BackSpace', 'Tab'):
        print(event.keysym)
        return 'break'

def calculate():
    volume1 = volume.get()
    abv1 = abv.get()
    alcohol_unit = (int(volume1)*int(abv1))/1000.0
    if alcohol_unit < 3:
        messagebox.showinfo(title='Result', message="It's okay to keep drinking.")
    elif alcohol_unit >= 3 and alcohol_unit < 4:
        messagebox.showinfo(title='Result', message="Enough drinking for today.")
    else:
        messagebox.showinfo(title='Result', message="For your good health, stop drinking NOW!")

root = Tk()
root.geometry('300x200+500+200')
root.title('Okay to Drink??')

volume = StringVar()
abv = StringVar()

empty0 = Label().pack()

label1 = Label(text='Volume (ml)').pack()
entry1 = Entry(textvariable=volume)
entry1.bind('<KeyPress>', keyPress)
entry1.pack()
entry1.focus()

empty1 = Label().pack()

label2 = Label(text='Alcohol by Volume (%/vol)').pack()
entry2 = Entry(textvariable=abv)
entry2.bind('<KeyPress>', keyPress)
entry2.pack()
entry2.focus()

empty2 = Label().pack()

#Menubar

menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Close", command = quit)
menubar.add_cascade(label = "File", menu = filemenu)

#Help Menu


helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help")
menubar.add_cascade(label = "Help", menu = helpmenu)

#About Menu

aboutmenu = Menu(menubar, tearoff = 0)
aboutmenu.add_command(label = "About")
menubar.add_cascade(label = "About", menu = aboutmenu)

root.config(menu = menubar)

mbutton = Button(text='OK', command=calculate).pack()
