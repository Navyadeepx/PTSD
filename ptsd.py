import os
import pickle 
import webbrowser
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
	e5=CTkEntry(ef1,placeholder_text='DD-MM-YYYY')
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
			stufile = open('stu.bin', 'ab')
			stu = {}
			stu['roll no.'] = e1.get()
			stu['name'] = e2.get()
			stu['class'] = e3.get()
			stu['section'] = e4.get()
			stu['d.o.b'] = e5.get()
			stu['gender'] = e6.get()
			pickle.dump(stu, stufile)
		x+=1
		b2.configure(state='disabled')
	x=0
	#buttons
	b1=CTkButton(ef1,text='Refresh',command=e,width=110)
	b2=CTkButton(ef1,text='Save',command=f,width=110)
	b1.grid(column=1,row=6,sticky='w')
	b2.grid(column=3,row=6,sticky='e')
e()
#Search
def s():
	Grid.columnconfigure(t.tab('Search'), 0, weight=1)
	Grid.rowconfigure(t.tab('Search'), 3, weight=1)
	sf1=CTkFrame(t.tab('Search'))
	sf1.grid(column=0,row=0,sticky='ew',pady=5)
	#option menu
	o1=CTkOptionMenu(sf1,
		  values=['roll no.','name','class','section','d.o.b','gender'],
		  width=110)
	o1.set('roll no.')
	o1.pack(side='left',padx=5)
	#entry widget
	e1=CTkEntry(sf1)
	e1.pack(side='left',expand=True,fill='x',pady=5)
	#go button function
	def f():
		nonlocal x
		if x==0:
			#display searched data
			sf2f1=CTkFrame(sf2)
			sf2f2=CTkFrame(sf2)
			sf2f3=CTkFrame(sf2)
			sf2f4=CTkFrame(sf2)
			sf2f5=CTkFrame(sf2)
			sf2f6=CTkFrame(sf2)
			sf2f1.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			sf2f2.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			sf2f3.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			sf2f4.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			sf2f5.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			sf2f6.pack(side='left',expand=True,fill='both',padx=5,pady=5)			
			sf2l1=CTkLabel(sf2f1,text='Roll No.')
			sf2l2=CTkLabel(sf2f2,text='Name')
			sf2l3=CTkLabel(sf2f3,text='Class')
			sf2l4=CTkLabel(sf2f4,text='Section')
			sf2l5=CTkLabel(sf2f5,text='D.O.B')
			sf2l6=CTkLabel(sf2f6,text='Gender')
			sf2l1.pack()
			sf2l2.pack()
			sf2l3.pack()
			sf2l4.pack()
			sf2l5.pack()
			sf2l6.pack()
			win.update()
			found = False
			if e1.get() == '/a':
				fin= open('stu.bin', 'ab+')
				fin.seek(0)
				try:
					while True:
						stu = pickle.load(fin)
						CTkLabel(sf2f1, text=stu['roll no.']).pack()
						CTkLabel(sf2f2, text=stu['name']).pack()
						CTkLabel(sf2f3, text=stu['class']).pack()
						CTkLabel(sf2f4, text=stu['section']).pack()
						CTkLabel(sf2f5, text=stu['d.o.b']).pack()
						CTkLabel(sf2f6, text=stu['gender']).pack()
				except EOFError:
					fin.close()
			else:
				fin = open('stu.bin', 'ab+')
				fin.seek(0)
				try:
					while True:
						stu = pickle.load(fin)
						if stu[o1.get()] == e1.get():
							CTkLabel(sf2f1, text=stu['roll no.']).pack()
							CTkLabel(sf2f2, text=stu['name']).pack()
							CTkLabel(sf2f3, text=stu['class']).pack()
							CTkLabel(sf2f4, text=stu['section']).pack()
							CTkLabel(sf2f5, text=stu['d.o.b']).pack()
							CTkLabel(sf2f6, text=stu['gender']).pack()
							found = True
				except EOFError:
					fin.close()
				finally:
					if found == False:
						sf2f1.destroy()
						sf2f2.destroy()
						sf2f3.destroy()
						sf2f4.destroy()
						sf2f5.destroy()
						sf2f6.destroy()
						l1 = CTkLabel(sf2, text='given entry not found',text_color='grey')
						l1.pack()
		x+=1
		b1.configure(state='disabled')
	x=0	
	#Go button
	b1=CTkButton(sf1,text='Go',width=110,command=f) 
	b1.pack(side='left',padx=5)
	#Results lable
	l1=CTkLabel(t.tab('Search'),text='Results')
	l1.grid(column=0,row=2,sticky='ew')
	#Results frame
	sf2=CTkFrame(t.tab('Search'))
	sf2.grid(column=0,row=3,sticky='news',pady=5)
	#Refresh Button
	b2=CTkButton(t.tab('Search'),text='Refresh',width=110,command=s)
	b2.grid(column=0,row=4,sticky='e')
s()
#update
def u():
	Grid.columnconfigure(t.tab('Update'), 0, weight=1)
	Grid.rowconfigure(t.tab('Update'), 1, weight=1)
	Grid.rowconfigure(t.tab('Update'), 3, weight=1)
	uf1=CTkFrame(t.tab('Update'))
	uf1.grid(column=0,row=0,sticky='ew',pady=5)
	#refresh button
	b0=CTkButton(uf1,text='Refresh',width=110,command=u)
	b0.pack(side='left',padx=5)
	#entry widget 1
	e1=CTkEntry(uf1,placeholder_text='Roll No.')
	e1.pack(side='left',expand=True,fill='x',pady=5)
	#Go button function
	def f1():
		nonlocal x
		if x==0:
			#display searched data
			uf2f1=CTkFrame(uf2,height=1)
			uf2f2=CTkFrame(uf2,height=1)
			uf2f3=CTkFrame(uf2,height=1)
			uf2f4=CTkFrame(uf2,height=1)
			uf2f5=CTkFrame(uf2,height=1)
			uf2f6=CTkFrame(uf2,height=1)
			uf2f1.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			uf2f2.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			uf2f3.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			uf2f4.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			uf2f5.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			uf2f6.pack(side='left',expand=True,fill='both',padx=5,pady=5)			
			uf2l1=CTkLabel(uf2f1,text='Roll No.')
			uf2l2=CTkLabel(uf2f2,text='Name')
			uf2l3=CTkLabel(uf2f3,text='Class')
			uf2l4=CTkLabel(uf2f4,text='Section')
			uf2l5=CTkLabel(uf2f5,text='D.O.B')
			uf2l6=CTkLabel(uf2f6,text='Gender')
			uf2l1.pack()
			uf2l2.pack()
			uf2l3.pack()
			uf2l4.pack()
			uf2l5.pack()
			uf2l6.pack()
			win.update()
			found = False
			fin = open('stu.bin', 'ab+')
			fin.seek(0)
			try:
				while True:
					stu = pickle.load(fin)
					if stu['roll no.'] == e1.get():
						CTkLabel(uf2f1, text=stu['roll no.']).pack()
						CTkLabel(uf2f2, text=stu['name']).pack()
						CTkLabel(uf2f3, text=stu['class']).pack()
						CTkLabel(uf2f4, text=stu['section']).pack()
						CTkLabel(uf2f5, text=stu['d.o.b']).pack()
						CTkLabel(uf2f6, text=stu['gender']).pack()
						found = True
						o1.configure(state='normal')
						e2.configure(state='normal')
						b2.configure(state='normal')
			except EOFError:
				fin.close()
			finally:
				if found == False:
					uf2f1.destroy()
					uf2f2.destroy()
					uf2f3.destroy()
					uf2f4.destroy()
					uf2f5.destroy()
					uf2f6.destroy()
					l1 = CTkLabel(uf2, text='given entry not found',text_color='grey')
					l1.pack()
		x+=1
		b1.configure(state='disabled')
	x=0	
	#Go button
	b1=CTkButton(uf1,text='Go',width=110,command=f1) 
	b1.pack(side='left',padx=5)
	#Results frame 1
	uf2=CTkFrame(t.tab('Update'),height=1)
	uf2.grid(column=0,row=1,sticky='news')
	uf3=CTkFrame(t.tab('Update'))
	uf3.grid(column=0,row=2,sticky='ew',pady=5)
	#option menu
	o1=CTkOptionMenu(uf3,
		  values=['name','class','section','d.o.b','gender'],
		  width=110,state='disabled')
	o1.set('name')
	o1.pack(side='left',padx=5)
	#entry widget 2
	e2=CTkEntry(uf3,state='disabled')
	e2.pack(side='left',expand=True,fill='x',pady=5)
	#Update button function
	def f2():
		nonlocal y
		if y==0 and f1()!=False:
			stu = {}
			stufile = open("stu.bin", "ab+")
			stufile.seek(0)
			try:
				bin = open("temp.tmp", "ab")
				while True:
					stu = pickle.load(stufile)
					if stu["roll no."] == e1.get():
						stu[o1.get()]=e2.get()
						uf4f1=CTkFrame(uf4,height=1)
						uf4f2=CTkFrame(uf4,height=1)
						uf4f3=CTkFrame(uf4,height=1)
						uf4f4=CTkFrame(uf4,height=1)
						uf4f5=CTkFrame(uf4,height=1)
						uf4f6=CTkFrame(uf4,height=1)
						uf4f1.pack(side='left',expand=True,fill='both',padx=5,pady=5)
						uf4f2.pack(side='left',expand=True,fill='both',padx=5,pady=5)
						uf4f3.pack(side='left',expand=True,fill='both',padx=5,pady=5)
						uf4f4.pack(side='left',expand=True,fill='both',padx=5,pady=5)
						uf4f5.pack(side='left',expand=True,fill='both',padx=5,pady=5)
						uf4f6.pack(side='left',expand=True,fill='both',padx=5,pady=5)			
						uf4l1=CTkLabel(uf4f1,text='Roll No.')
						uf4l2=CTkLabel(uf4f2,text='Name')
						uf4l3=CTkLabel(uf4f3,text='Class')
						uf4l4=CTkLabel(uf4f4,text='Section')
						uf4l5=CTkLabel(uf4f5,text='D.O.B')
						uf4l6=CTkLabel(uf4f6,text='Gender')
						uf4l1.pack()
						uf4l2.pack()
						uf4l3.pack()
						uf4l4.pack()
						uf4l5.pack()
						uf4l6.pack()
						CTkLabel(uf4f1, text=stu['roll no.']).pack()
						CTkLabel(uf4f2, text=stu['name']).pack()
						CTkLabel(uf4f3, text=stu['class']).pack()
						CTkLabel(uf4f4, text=stu['section']).pack()
						CTkLabel(uf4f5, text=stu['d.o.b']).pack()
						CTkLabel(uf4f6, text=stu['gender']).pack()
					pickle.dump(stu, bin)
			except EOFError:
				stufile.close()
		bin.close()
		os.remove("stu.bin")
		os.rename("temp.tmp", "stu.bin")
		y+=1
		b2.configure(state='disabled')
	y=0
	#Update button
	b2=CTkButton(uf3,text='Update',width=110,command=f2,state='disabled') 
	b2.pack(side='left',padx=5)
	#results frame 2
	uf4=CTkFrame(t.tab('Update'),height=1)
	uf4.grid(column=0,row=3,sticky='news')
u()
#delete
def d():
	Grid.columnconfigure(t.tab('Delete'), 0, weight=1)
	df1=CTkFrame(t.tab('Delete'))
	df1.grid(column=0,row=0,sticky='ew',pady=5)
	#refresh button
	b0=CTkButton(df1,text='Refresh',width=110,command=d)
	b0.pack(side='left',padx=5)
	#entry widget 1
	e1=CTkEntry(df1,placeholder_text='Roll No.')
	e1.pack(side='left',expand=True,fill='x',pady=5)
	#Go button function
	def f1():
		nonlocal x
		if x==0:
			#display searched data
			df2f1=CTkFrame(df2,height=1)
			df2f2=CTkFrame(df2,height=1)
			df2f3=CTkFrame(df2,height=1)
			df2f4=CTkFrame(df2,height=1)
			df2f5=CTkFrame(df2,height=1)
			df2f6=CTkFrame(df2,height=1)
			df2f1.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			df2f2.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			df2f3.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			df2f4.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			df2f5.pack(side='left',expand=True,fill='both',padx=5,pady=5)
			df2f6.pack(side='left',expand=True,fill='both',padx=5,pady=5)			
			df2l1=CTkLabel(df2f1,text='Roll No.')
			df2l2=CTkLabel(df2f2,text='Name')
			df2l3=CTkLabel(df2f3,text='Class')
			df2l4=CTkLabel(df2f4,text='Section')
			df2l5=CTkLabel(df2f5,text='D.O.B')
			df2l6=CTkLabel(df2f6,text='Gender')
			df2l1.pack()
			df2l2.pack()
			df2l3.pack()
			df2l4.pack()
			df2l5.pack()
			df2l6.pack()
			win.update()
			found = False
			fin = open('stu.bin', 'ab+')
			fin.seek(0)
			try:
				while True:
					stu = pickle.load(fin)
					if stu['roll no.'] == e1.get():
						CTkLabel(df2f1, text=stu['roll no.']).pack()
						CTkLabel(df2f2, text=stu['name']).pack()
						CTkLabel(df2f3, text=stu['class']).pack()
						CTkLabel(df2f4, text=stu['section']).pack()
						CTkLabel(df2f5, text=stu['d.o.b']).pack()
						CTkLabel(df2f6, text=stu['gender']).pack()
						found = True
						b2.configure(state='normal')
			except EOFError:
				fin.close()
			finally:
				if found == False:
					df2f1.destroy()
					df2f2.destroy()
					df2f3.destroy()
					df2f4.destroy()
					df2f5.destroy()
					df2f6.destroy()
					l1 = CTkLabel(df2, text='given entry not found',text_color='grey')
					l1.pack(pady=5)
		x+=1
		b1.configure(state='disabled')
	x=0	
	#Go button
	b1=CTkButton(df1,text='Go',width=110,command=f1) 
	b1.pack(side='left',padx=5)
	#Results frame
	df2=CTkFrame(t.tab('Delete'),height=38)
	df2.grid(column=0,row=1,sticky='news',pady=5)
	#Delete frame 
	df3=CTkFrame(t.tab('Delete'))
	df3.grid(column=0,row=2,sticky='ew',pady=5)
	#Delete warning label
	l1=CTkLabel(df3,text='This action can not be un-done',
	     text_color='grey')
	l1.pack(padx=10,side='left')
	#Delete button function
	def f2():
		stu = {}
		stufile = open("stu.bin", "ab+")
		try:
			bin = open("temp.tmp", "ab")
			while True:
				stu = pickle.load(stufile)
				if stu["roll no"] == e1.get():
					stu.clear()
		except EOFError:
			stufile.close()
		bin.close()
		os.remove("stu.bin")
		os.rename("temp.tmp", "stu.bin")
		b2.configure(text='Done!',state='disabled')
	#Delete button
	b2=CTkButton(df3,text='DELETE',fg_color='red',width=110,
		  text_color='black',
		  hover_color='dark red',
		  command=f2,
		  state='disabled')
	b2.pack(pady=5,padx=5,side='right')
d()
#info
if1=CTkFrame(t.tab('Info'))
if1.pack(expand=True)
str='''PTSD
Ver.6.5

Python Tkinter Student Database

simple student database management program made
with pythonand CustomTkinter module'''
#info text
il1=CTkLabel(if1,text=str)
il1.pack(expand=True,padx=10,pady=10)
#github link button function
def f():
	webbrowser.open('https://github.com/Navyadeepx/PTSD')  
#github link button
ib1=CTkButton(if1,text='GitHub 🔗',command=f)
ib1.pack(pady=10)
win.mainloop()
