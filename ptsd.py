import pickle
import os 
from tkinter import *
from ttkbootstrap import *

#window
win=Window(themename='my')
win.geometry('600x400')
win.minsize(600,400)
win.attributes('-topmost',True)
win.title('PTSD')
win.iconbitmap('logo.ico')
#menu
menu=Menu(win,fg='#353535')
#sub_menu_file
filemenu=Menu(menu,tearoff=False)
filemenu.add_command(label='New',command=lambda:print('New'))
filemenu.add_command(label='Open',command=lambda:print('Open'))
filemenu.add_command(label='Save',command=lambda:print('Save'))
filemenu.add_command(label='Save as',command=lambda:print('Save as'))
filemenu.add_separator()
filemenu.add_command(label='Quit',command=win.quit)
menu.add_cascade(label='File',menu=filemenu)
#sub_menus
menu.add_command(label='Enter',command=lambda:print('Enter'))
menu.add_command(label='Search',command=lambda:print('Search'))
menu.add_command(label='Update',command=lambda:print('Update'))
menu.add_command(label='Update',command=lambda:print('Update'))
menu.add_command(label='Help',command=lambda:print('Help'))


win.configure(menu=menu)

win.mainloop()