import os
import pickle 
from tkinter import *
from customtkinter import *
#window
win=CTk()
win.geometry()
win.minsize(600,445)
win.attributes('-topmost',True)
win.title('PTSD')
#tabs
t=CTkTabview(win)
t.pack(fill='both',expand=True)
t.add('Enter')
t.add('Search')
t.add('Update')
t.add('Delete')
t.add('Info')
#enter
def e():
	Grid.columnconfigure(t.tab('Enter'), 0, weight=1)
	ef1=CTkFrame(t.tab('Enter'))
	ef2=CTkFrame(t.tab('Enter'),height=40)
	ef1.grid(column=0,row=0,sticky='news',ipady=5)
	ef2.grid(column=0,row=2,sticky='news')
	el1=CTkLabel(t.tab('Enter'),text='Entered data')
	el1.grid(column=0,row=1,sticky='ew')
	Grid.columnconfigure(ef1, 0, weight=1)
	Grid.columnconfigure(ef1, 1, weight=1)
	Grid.columnconfigure(ef1, 2, weight=1)
	Grid.columnconfigure(ef1, 3, weight=1)
	Grid.columnconfigure(ef1, 4, weight=1)
	#entry widget lables
	ef1l0=CTkLabel(ef1,text='',width=40,height=5)
	ef1l1=CTkLabel(ef1,text='Roll No. :')
	ef1l2=CTkLabel(ef1,text='Name :')
	ef1l3=CTkLabel(ef1,text='Class :')
	ef1l4=CTkLabel(ef1,text='Section :')
	ef1l5=CTkLabel(ef1,text='D.O.B :')
	ef1l6=CTkLabel(ef1,text='Gender :')
	ef1l0.grid(column=4,row=0,pady=8,padx=5,sticky='e')
	ef1l1.grid(column=0,row=0,pady=8,padx=5,sticky='e')
	ef1l2.grid(column=0,row=1,pady=8,padx=5,sticky='e')
	ef1l3.grid(column=0,row=2,pady=8,padx=5,sticky='e')
	ef1l4.grid(column=0,row=3,pady=8,padx=5,sticky='e')
	ef1l5.grid(column=0,row=4,pady=8,padx=5,sticky='e')
	ef1l6.grid(column=0,row=5,pady=8,padx=5,sticky='e')
	#entry widgets
	e1=CTkEntry(ef1)
	e2=CTkEntry(ef1)
	e3=CTkEntry(ef1)
	e4=CTkEntry(ef1)
	e5=CTkEntry(ef1)
	e6=CTkEntry(ef1)
	e1.grid(column=1,row=0,columnspan=3,sticky='ew')
	e2.grid(column=1,row=1,columnspan=3,sticky='ew')
	e3.grid(column=1,row=2,columnspan=3,sticky='ew')
	e4.grid(column=1,row=3,columnspan=3,sticky='ew')
	e5.grid(column=1,row=4,columnspan=3,sticky='ew')
	e6.grid(column=1,row=5,columnspan=3,sticky='ew')
	#save button function
	def f():
		nonlocal x
		if x==0:
			#display entered data
			ef2f1=CTkFrame(ef2,height=30,width=50)
			ef2f2=CTkFrame(ef2,height=30,width=50)
			ef2f3=CTkFrame(ef2,height=30,width=50)
			ef2f4=CTkFrame(ef2,height=30,width=50)
			ef2f5=CTkFrame(ef2,height=30,width=50)
			ef2f6=CTkFrame(ef2,height=30,width=50)
			ef2f1.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			ef2f2.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			ef2f3.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			ef2f4.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			ef2f5.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			ef2f6.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			ef2l1=CTkLabel(ef2f1,text='Roll No.')
			ef2l2=CTkLabel(ef2f2,text='Name')
			ef2l3=CTkLabel(ef2f3,text='Class')
			ef2l4=CTkLabel(ef2f4,text='Section')
			ef2l5=CTkLabel(ef2f5,text='D.O.B')
			ef2l6=CTkLabel(ef2f6,text='Gender')
			ef2l1.pack()
			ef2l2.pack()
			ef2l3.pack()
			ef2l4.pack()
			ef2l5.pack()
			ef2l6.pack()
			ef2l10=CTkLabel(ef2f1,text=e1.get())
			ef2l11=CTkLabel(ef2f2,text=e2.get())
			ef2l12=CTkLabel(ef2f3,text=e3.get())
			ef2l13=CTkLabel(ef2f4,text=e4.get())
			ef2l14=CTkLabel(ef2f5,text=e5.get())
			ef2l15=CTkLabel(ef2f6,text=e6.get())
			ef2l10.pack()
			ef2l11.pack()
			ef2l12.pack()
			ef2l13.pack()
			ef2l14.pack()
			ef2l15.pack()
			stufile = open("stu.bin", "ab")
			stu = {}
			stu["roll no"] = e1.get()
			stu["name"] = e2.get()
			stu["class"] = e3.get()
			stu["section"] = e4.get()
			stu["d.o.b"] = e5.get()
			stu["gender"] = e6.get()
			pickle.dump(stu, stufile)
		x+=1
	x=0
	#buttons
	b2=CTkButton(ef1,text='Save',command=f,width=110)
	b1=CTkButton(ef1,text='Refresh',command=e,width=110)
	b1.grid(column=1,row=6,sticky='w')
	b2.grid(column=3,row=6,sticky='e')
e()
#Search
def s():
	Grid.columnconfigure(t.tab('Search'), 0, weight=1)
	Grid.rowconfigure(t.tab('Search'), 3, weight=1)
	sf1=CTkFrame(t.tab('Search'))
	sf1.grid(column=0,row=0,sticky='ew')
	#option menu function
	def o1f(choice):
		return choice
	#option menu
	o1=CTkOptionMenu(sf1,
		  values=['Roll No.','Name','Class','Section','D.O.B','Gender'],
		  command=o1f,
		  width=110)
	o1.set('Roll No.')
	o1.pack(side='left',padx=5)
	#entry widget
	e1=CTkEntry(sf1)
	e1.pack(side='left',expand=True,fill='x',pady=5)
	#Go button
	b1=CTkButton(sf1,text='Go',width=110) 
	b1.pack(side='left',padx=5)
	#Results lable
	l1=CTkLabel(t.tab('Search'),text='Results')
	l1.grid(column=0,row=2,sticky='ew')
	#Results frame
	sf2=CTkFrame(t.tab('Search'))
	sf2.grid(column=0,row=3,sticky='news',pady=5)
	#Refresh Button
	b2=CTkButton(t.tab('Search'),text='Refresh',width=110)
	b2.grid(column=0,row=4,sticky='e')
s()
win.mainloop()