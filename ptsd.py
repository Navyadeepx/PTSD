import pickle 
from tkinter import *
from ttkbootstrap import *

#window
win=Window(themename='my')
win.geometry('600x400')

t=Notebook(win,width=600, height=400)
t.pack(fill='both',expand=True)

f1=Frame(t)
f1.pack()
f2=Frame(t)
f2.pack()
f3=Frame(t)
f3.pack()
f4=Frame(t)
f4.pack()

t.add(f1,text='Enter')
t.add(f2,text='Search')
t.add(f3,text='Update')
t.add(f4,text='Delete')

win.mainloop()