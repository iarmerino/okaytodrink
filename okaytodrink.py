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
root.geometry('350x400+500+200')
root.title('Okay to Drink??')

volume = StringVar()
abv = StringVar()
unit = StringVar()
unit.set("mL")


img = PhotoImage(file="banner.gif")
mlabel = Label(root, image=img)
mlabel.place(x=20, y=1)


label1 = Label(text='Volume').place(x=140, y=210)
entry1 = Entry(textvariable=volume, width=15)
entry1.bind('<KeyPress>', keyPress)
entry1.place(x=100, y=240)
entry1.focus()

unit_option = OptionMenu(root, unit, "mL", "glass", "bottle", "shot")
unit_option.place(x=200, y=230)

label2 = Label(text='Alcohol by Volume (%/vol)').place(x=90, y=270)
entry2 = Entry(textvariable=abv, width=25)
entry2.bind('<KeyPress>', keyPress)
entry2.place(x=100, y=300)


mbutton = Button(text='Okay to drink?', command=calculate).place(x=130, y=350)

#Menubar

menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Close", command = quit)
menubar.add_cascade(label = "File", menu = filemenu)

#Help Menu

def menu_help():
    messagebox.showinfo(title='Help', message="How to use this program")
    return

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help", command = menu_help)
menubar.add_cascade(label = "Help", menu = helpmenu)

#About Menu

def menu_about():
    messagebox.showinfo(title='About', message="Created By\nKarn Niamchan 57070004\nJirapat Kuengwong 57070021")
    return
    
aboutmenu = Menu(menubar, tearoff = 0)
aboutmenu.add_command(label = "About", command = menu_about)
menubar.add_cascade(label = "About", menu = aboutmenu)

root.config(menu = menubar)

