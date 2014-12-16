import sys
from tkinter import *

def keyPress(event):
    if event.char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print(event.char)
    elif event.keysym not in ('Alt_r', 'Alt_l', 'F4', 'BackSpace', 'Tab'):
        print(event.keysym)
        return 'break'

def enableEntry():
    '''enable entry box'''
    entry2.configure(state='normal')
    entry2.update()
    
def disableEntry():
    '''disable entry box'''
    entry2.configure(state='disabled')
    entry2.update()

def checkblank():
    '''check if there is one of entry boxes is empty'''
    if volume.get() == '' and abv.get() == '' and select.get() == 2:
        messagebox.showwarning(title='Warning', message="Please insert volume and alcohol by volume.")
    elif volume.get() == '':
        messagebox.showwarning(title='Warning', message="Please insert volume.")
    elif abv.get() == '' and select.get() == 2:
        messagebox.showwarning(title='Warning', message="Please insert alcohol by volume")
    else:
        calculate()
        
def calculate():
    '''calculate the alcohol unit'''
    abv1 = 0
    volume1 = float(volume.get())
    if unit.get() == 'glass(es)':
        volume1 *= 250
    elif unit.get() == 'bottle(s)':
        volume1 *= 640
    elif unit.get() == 'shot(s)':
        volume1 *= 44

    if select.get() == 1:
        if alc_type.get() == 'Beer (5 %/v)':
            abv1 = 5.0
        elif alc_type.get() == 'Wine (13 %/v)':
            abv1 = 13.0
        elif alc_type.get() == 'Whiskey (40 %/v)':
            abv1 = 40.0
        elif alc_type.get() == 'Vodka (45 %/v)':
            abv1 = 45.0
    else:
        abv1 = float(abv.get())
       
    alcohol_unit = (volume1*abv1)/1000.0
    if alcohol_unit < 4:
        messagebox.showinfo(title='Result', message="It's okay to keep drinking.")
    else:
        messagebox.showinfo(title='Result', message="Enough drinking for today.")
        
root = Tk()
root.geometry('350x400+500+200')
root.title('Okay to Drink??')

volume = StringVar()
abv = StringVar()
unit = StringVar()
unit.set('mL')
alc_type = StringVar()
alc_type.set('Beer (5 %/v)')
select = IntVar()

img = PhotoImage(file="new_banner.gif")
mlabel = Label(root, image=img)
mlabel.place(x=3, y=1)

label1 = Label(text='Insert volume').place(x=135, y=145)
entry1 = Entry(textvariable=volume, width=15)
entry1.bind('<KeyPress>', keyPress)
entry1.place(x=100, y=180)
entry1.focus()

unit_option = OptionMenu(root, unit, 'mL', 'glass(es)', 'bottle(s)', 'shot(s)')
unit_option.place(x=200, y=175)

radbutton1 = Radiobutton(root, text='Select a type of alcohol', variable=select, value=1, command=disableEntry)
radbutton1.place(x=30, y=233)
radbutton1.select()

type_option = OptionMenu(root, alc_type, 'Beer (5 %/v)', 'Wine (13 %/v)', 'Whiskey (40 %/v)', 'Vodka (45 %/v)')
type_option.place(x=190, y=230)

radbutton2 = Radiobutton(root, text='Insert Alcohol by Volume (%/v)', variable=select, value=2, command=enableEntry)
radbutton2.place(x=30, y=270)

entry2 = Entry(textvariable=abv, width=10, state='disabled')
entry2.bind('<KeyPress>', keyPress)
entry2.place(x=230, y=273)

mbutton = Button(text='Okay to drink?', command=checkblank).place(x=130, y=330)

#Menubar

menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Close", command = quit)
menubar.add_cascade(label = "File", menu = filemenu)

#Help Menu

def menu_help():
    messagebox.showinfo(title='How to use this program',
    message="How to use this program\n\n1. Insert volume and select its unit.\n2. Choose to select type of alcohol or insert alcohol by volume.\n3. Click \"Okay to drink?\" button.")
    return

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "How to use", command = menu_help)
menubar.add_cascade(label = "Help", menu = helpmenu)

#About Menu

def menu_about():
    messagebox.showinfo(title='About this program',
    message="Created By...\n\nKarn Niamchan         57070004\nJirapat Kuengwong   57070021")
    return
    
aboutmenu = Menu(menubar, tearoff = 0)
aboutmenu.add_command(label = "About this program", command = menu_about)
menubar.add_cascade(label = "About", menu = aboutmenu)

root.config(menu = menubar)
