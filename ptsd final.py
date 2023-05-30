from tkinter import *
from ttkbootstrap import *
import pymysql as pym

# my sql connection with python using pymysql
conn = pym.connect(
	host="localhost",
	user="root",
	password="0pl,0pl,",
	database="db2",
)
cur = conn.cursor()

root = Tk()
root.geometry("600x400")
root.configure(bg="#1b1b1b")
root.title("P.T.S.D. MySql ver. (dark)")
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)

a1 = Label(root, text='"Choose any tab to continue"', bg="#1b1b1b", fg="grey")
a1.grid(row=4, column=0, sticky="EW", columnspan=4)

def f0():
	for Widget in root.winfo_children():
		Widget.destroy()
	Button(root, text="Enter", command=f1, bg="#1b1b1b", fg="white").grid(
		row=0, column=0, sticky="EW"
	)
	Button(root, text="Search", command=f2, bg="#1b1b1b", fg="white").grid(
		row=0, column=1, sticky="EW"
	)
	Button(root, text="Update", command=f3, bg="#1b1b1b", fg="white").grid(
		row=0, column=2, sticky="EW"
	)
	Button(root, text="Delete", command=f4, bg="#1b1b1b", fg="white").grid(
		row=0, column=3, sticky="EW"
	)

# ENTER
def f1():
	f0()
	Grid.rowconfigure(root, 4, weight=0)
	b1 = Button(root, text="Enter", bg="#1b1b1b", fg="grey", relief=SUNKEN, command=f1)
	b1.grid(row=0, column=0, sticky="EW")
	Label(root, bg="#1b1b1b", fg="white").grid(row=11, column=0, columnspan=4)
	f = LabelFrame(root, text="Entered data", bg="#1b1b1b", fg="white")
	f.grid(row=12, column=0, rowspan=8, columnspan=4, sticky="EWNS", padx=5, pady=5)
	Grid.columnconfigure(f, 0, weight=1)
	Grid.columnconfigure(f, 1, weight=1)
	Grid.columnconfigure(f, 2, weight=1)
	Grid.columnconfigure(f, 3, weight=1)
	Grid.columnconfigure(f, 4, weight=1)
	Grid.columnconfigure(f, 5, weight=1)
	Grid.columnconfigure(f, 6, weight=1)
	Label(f, bg="#1b1b1b", fg="white").grid(row=0, column=0, columnspan=8)
	Label(root, text="", bg="#1b1b1b", fg="white").grid(row=1, column=0)
	Label(root, text="Roll no.: ", bg="#1b1b1b", fg="white").grid(row=2, column=0)
	Label(root, text="Name: ", bg="#1b1b1b", fg="white").grid(row=3, column=0)
	Label(root, text="Class: ", bg="#1b1b1b", fg="white").grid(row=4, column=0)
	Label(root, text="D.O.B.: ", bg="#1b1b1b", fg="white").grid(row=5, column=0)
	Label(root, text="Gender: ", bg="#1b1b1b", fg="white").grid(row=6, column=0)
	Label(root, text="House: ", bg="#1b1b1b", fg="white").grid(row=7, column=0)
	Label(root, text="Subject: ", bg="#1b1b1b", fg="white").grid(row=8, column=0)
	e1 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e1.grid(row=2, column=1, columnspan=2, sticky="EW")
	e2 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e2.grid(row=3, column=1, columnspan=2, sticky="EW")
	e3 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e3.grid(row=4, column=1, columnspan=2, sticky="EW")
	e4 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e4.insert(0, "yyyy-dd-mm")
	e4.grid(row=5, column=1, columnspan=2, sticky="EW")
	e5 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e5.grid(row=6, column=1, columnspan=2, sticky="EW")
	e6 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e6.grid(row=7, column=1, columnspan=2, sticky="EW")
	e7 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e7.grid(row=8, column=1, columnspan=2, sticky="EW")

	def f1_1():
		st = "insert into ptsd values('{}','{}','{}','{}','{}','{}','{}')".format(
			e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get()
		)
		cur.execute(st)
		conn.commit()
		f1_1 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_1.grid(row=1, column=0, sticky="EW")
		Label(f, text="Roll no.", bg="#1b1b1b", fg="white").grid(
			row=0, column=0, sticky="EW"
		)
		Label(f1_1, text=e1.get(), bg="#1b1b1b", fg="white").pack()
		f1_2 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_2.grid(row=1, column=1, sticky="EW")
		Label(f, text="Name", bg="#1b1b1b", fg="white").grid(row=0, column=1, sticky="EW")
		Label(f1_2, text=e2.get(), bg="#1b1b1b", fg="white").pack()
		f1_3 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_3.grid(row=1, column=2, sticky="EW")
		Label(f, text="Class", bg="#1b1b1b", fg="white").grid(
			row=0, column=2, sticky="EW"
		)
		Label(f1_3, text=e3.get(), bg="#1b1b1b", fg="white").pack()
		f1_4 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_4.grid(row=1, column=3, sticky="EW")
		Label(f, text="D.O.B.", bg="#1b1b1b", fg="white").grid(
			row=0, column=3, sticky="EW"
		)
		Label(f1_4, text=e4.get(), bg="#1b1b1b", fg="white").pack()
		f1_5 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_5.grid(row=1, column=4, sticky="EW")
		Label(f, text="Gender", bg="#1b1b1b", fg="white").grid(
			row=0, column=4, sticky="EW"
		)
		Label(f1_5, text=e5.get(), bg="#1b1b1b", fg="white").pack()
		f1_6 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_6.grid(row=1, column=5, sticky="EW")
		Label(f, text="House", bg="#1b1b1b", fg="white").grid(
			row=0, column=5, sticky="EW"
		)
		Label(f1_6, text=e6.get(), bg="#1b1b1b", fg="white").pack()
		f1_7 = LabelFrame(f, bg="#1b1b1b", fg="white")
		f1_7.grid(row=1, column=6, sticky="EW")
		Label(f, text="Subject", bg="#1b1b1b", fg="white").grid(
			row=0, column=6, sticky="EW"
		)
		Label(f1_7, text=e7.get(), bg="#1b1b1b", fg="white").pack()

	b2 = Button(root, text="Save", width=10, command=f1_1, bg="#1b1b1b", fg="white")
	b2.grid(row=10, column=2, sticky="E")
	b3 = Button(root, text="refresh", width=10, command=f1, bg="#1b1b1b", fg="white")
	b3.grid(row=10, column=1, sticky="W")

Button(root, text="Enter", command=f1, bg="#1b1b1b", fg="white").grid(
	row=0, column=0, sticky="EW"
)

# SEARCH
def f2():
	f0()
	Grid.rowconfigure(root, 4, weight=1)
	b1 = Button(root, text="Search", bg="#1b1b1b", fg="grey", relief=SUNKEN, command=f2)
	b1.grid(row=0, column=1, sticky="EW")
	f1 = LabelFrame(root, text="results", padx=5, bg="#1b1b1b", fg="white")
	f1.grid(row=4, column=0, rowspan=8, columnspan=4, sticky="EWNS", padx=5, pady=5)
	Grid.columnconfigure(f1, 0, weight=1)
	Grid.columnconfigure(f1, 1, weight=1)
	Grid.columnconfigure(f1, 2, weight=1)
	Grid.columnconfigure(f1, 3, weight=1)
	Grid.columnconfigure(f1, 4, weight=1)
	Grid.columnconfigure(f1, 5, weight=1)
	Grid.columnconfigure(f1, 6, weight=1)
	Label(root, bg="#1b1b1b", fg="white").grid(row=1, column=0)
	c1 = StringVar()
	c1.set("rollno")
	c2 = OptionMenu(
		root, c1, "rollno", "name", "class", "dob", "gender", "house", "subject"
	)
	c2.grid(
		row=2,
		column=0,
		sticky="EW",
		padx=5,
	)
	e1 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e1.grid(row=2, column=1, columnspan=2, sticky="EW")
	c2.configure(
		bg="#1b1b1b",
		fg="white",
		activebackground="#1b1b1b",
	)

	def f2_1():
		f1_1 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_1.grid(row=1, column=0, sticky="EW")
		Label(f1, text="Roll no.", bg="#1b1b1b", fg="white").grid(
			row=0, column=0, sticky="EW"
		)
		f1_2 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_2.grid(row=1, column=1, sticky="EW")
		Label(f1, text="Name", bg="#1b1b1b", fg="white").grid(
			row=0, column=1, sticky="EW"
		)
		f1_3 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_3.grid(row=1, column=2, sticky="EW")
		Label(f1, text="Class", bg="#1b1b1b", fg="white").grid(
			row=0, column=2, sticky="EW"
		)
		f1_4 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_4.grid(row=1, column=3, sticky="EW")
		Label(f1, text="D.O.B.", bg="#1b1b1b", fg="white").grid(
			row=0, column=3, sticky="EW"
		)
		f1_5 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_5.grid(row=1, column=4, sticky="EW")
		Label(f1, text="Gender", bg="#1b1b1b", fg="white").grid(
			row=0, column=4, sticky="EW"
		)
		f1_6 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_6.grid(row=1, column=5, sticky="EW")
		Label(f1, text="House", bg="#1b1b1b", fg="white").grid(
			row=0, column=5, sticky="EW"
		)
		f1_7 = LabelFrame(f1, bg="#1b1b1b", fg="white")
		f1_7.grid(row=1, column=6, sticky="EW")
		Label(f1, text="Subject", bg="#1b1b1b", fg="white").grid(
			row=0, column=6, sticky="EW"
		)
		if e1.get() == "/a":
			cur.execute("SELECT * FROM ptsd;")
			data = cur.fetchall()
			for i in data:
				Label(f1_1, text=i[0], bg="#1b1b1b", fg="white").pack()
				Label(f1_2, text=i[1], bg="#1b1b1b", fg="white").pack()
				Label(f1_3, text=i[2], bg="#1b1b1b", fg="white").pack()
				Label(f1_4, text=i[3], bg="#1b1b1b", fg="white").pack()
				Label(f1_5, text=i[4], bg="#1b1b1b", fg="white").pack()
				Label(f1_6, text=i[5], bg="#1b1b1b", fg="white").pack()
				Label(f1_7, text=i[6], bg="#1b1b1b", fg="white").pack()
		else:
			cur.execute('SELECT * FROM ptsd where {} = "{}"'.format(c1.get(), e1.get()))
			data = cur.fetchall()
			if cur.rowcount == 0:
				l1 = Label(
					f1,
					text="given entry not found",
					bg="#1b1b1b",
					fg="white",
				)
				l1.grid(row=1, column=0, sticky="EW", columnspan=7)
			for i in data:
				Label(f1_1, text=i[0], bg="#1b1b1b", fg="white").pack()
				Label(f1_2, text=i[1], bg="#1b1b1b", fg="white").pack()
				Label(f1_3, text=i[2], bg="#1b1b1b", fg="white").pack()
				Label(f1_4, text=i[3], bg="#1b1b1b", fg="white").pack()
				Label(f1_5, text=i[4], bg="#1b1b1b", fg="white").pack()
				Label(f1_6, text=i[5], bg="#1b1b1b", fg="white").pack()
				Label(f1_7, text=i[6], bg="#1b1b1b", fg="white").pack()

	b2 = Button(root, text="Go", command=f2_1, bg="#1b1b1b", fg="white")
	b2.grid(row=2, column=3, sticky="EW", padx=5)
	b3 = Button(root, text="refresh", command=f2, bg="#1b1b1b", fg="white")
	b3.grid(row=90, column=3, sticky="EW", padx=5, pady=5)

Button(root, text="Search", command=f2, bg="#1b1b1b", fg="white").grid(
	row=0, column=1, sticky="EW"
)

# UPDATE
def f3():
	f0()
	Grid.rowconfigure(root, 4, weight=0)
	b1 = Button(root, text="Update", bg="#1b1b1b", fg="grey", relief=SUNKEN, command=f3)
	b1.grid(row=0, column=2, sticky="EW")
	f1 = LabelFrame(root, text="results", bg="#1b1b1b", fg="white")
	f1.grid(row=3, column=0, columnspan=4, sticky="EW", padx=5, pady=5)
	Grid.columnconfigure(f1, 0, weight=1)
	Grid.columnconfigure(f1, 1, weight=1)
	Grid.columnconfigure(f1, 2, weight=1)
	Grid.columnconfigure(f1, 3, weight=1)
	Grid.columnconfigure(f1, 4, weight=1)
	Grid.columnconfigure(f1, 5, weight=1)
	Grid.columnconfigure(f1, 6, weight=1)
	Label(f1, bg="#1b1b1b", fg="white").grid(row=0, column=0, columnspan=8)
	f2 = LabelFrame(root, text="results", bg="#1b1b1b", fg="white")
	f2.grid(row=5, column=0, columnspan=4, sticky="EW", padx=5, pady=5)
	Grid.columnconfigure(f2, 0, weight=1)
	Grid.columnconfigure(f2, 1, weight=1)
	Grid.columnconfigure(f2, 2, weight=1)
	Grid.columnconfigure(f2, 3, weight=1)
	Grid.columnconfigure(f2, 4, weight=1)
	Grid.columnconfigure(f2, 5, weight=1)
	Grid.columnconfigure(f2, 6, weight=1)
	Label(f2, bg="#1b1b1b", fg="white").grid(row=0, column=0, columnspan=8)
	Label(root, bg="#1b1b1b", fg="white").grid(row=1, column=0)
	fb = LabelFrame(root, bg="#1b1b1b", fg="white")
	fb.grid(row=2, column=0, sticky="EW", padx=5)
	Grid.columnconfigure(fb, 0, weight=1)
	Grid.columnconfigure(fb, 1, weight=1)
	Label(fb, text="Search:", width=1, bg="#1b1b1b", fg="white").grid(
		row=0, column=1, sticky="Ew"
	)
	e1 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e1.grid(row=2, column=1, columnspan=2, sticky="EW")

	def f3_1():
		cur.execute("SELECT * FROM ptsd where rollno = {};".format(e1.get()))
		data = cur.fetchall()
		if cur.rowcount == 0:
			Label(root, text="not found", bg="#1b1b1b", fg="white").grid(
				row=3, column=1, columnspan=2
			)
		for i in data:
			Label(root, text="not found", bg="#1b1b1b", fg="white").destroy()
			f1_1 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_1.grid(row=1, column=0, sticky="EW")
			Label(f1, text="Roll no.", bg="#1b1b1b", fg="white").grid(
				row=0, column=0, sticky="EW"
			)
			Label(f1_1, text=i[0], bg="#1b1b1b", fg="white").pack()
			f1_2 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_2.grid(row=1, column=1, sticky="EW")
			Label(f1, text="Name", bg="#1b1b1b", fg="white").grid(
				row=0, column=1, sticky="EW"
			)
			Label(f1_2, text=i[1], bg="#1b1b1b", fg="white").pack()
			f1_3 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_3.grid(row=1, column=2, sticky="EW")
			Label(f1, text="Class", bg="#1b1b1b", fg="white").grid(
				row=0, column=2, sticky="EW"
			)
			Label(f1_3, text=i[2], bg="#1b1b1b", fg="white").pack()
			f1_4 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_4.grid(row=1, column=3, sticky="EW")
			Label(f1, text="D.O.B.", bg="#1b1b1b", fg="white").grid(
				row=0, column=3, sticky="EW"
			)
			Label(f1_4, text=i[3], bg="#1b1b1b", fg="white").pack()
			f1_5 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_5.grid(row=1, column=4, sticky="EW")
			Label(f1, text="Gender", bg="#1b1b1b", fg="white").grid(
				row=0, column=4, sticky="EW"
			)
			Label(f1_5, text=i[4], bg="#1b1b1b", fg="white").pack()
			f1_6 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_6.grid(row=1, column=5, sticky="EW")
			Label(f1, text="House", bg="#1b1b1b", fg="white").grid(
				row=0, column=5, sticky="EW"
			)
			Label(f1_6, text=i[5], bg="#1b1b1b", fg="white").pack()
			f1_7 = LabelFrame(f1, bg="#1b1b1b", fg="white")
			f1_7.grid(row=1, column=6, sticky="EW")
			Label(f1, text="Subject", bg="#1b1b1b", fg="white").grid(
				row=0, column=6, sticky="EW"
			)
			Label(f1_7, text=i[6], bg="#1b1b1b", fg="white").pack()

	c1 = StringVar()
	c1.set("name")
	c2 = OptionMenu(root, c1, "name", "class", "dob", "gender", "house", "subject")
	c2.grid(
		row=4,
		column=0,
		sticky="EW",
	)
	c2.configure(bg="#1b1b1b", fg="white", activebackground="#1b1b1b")
	e2 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e2.grid(row=4, column=1, columnspan=2, sticky="EW", padx=5)

	def f3_2():
		cur.execute(
			"UPDATE ptsd SET {} = '{}' WHERE rollno = {}".format(
				c1.get(), e2.get(), e1.get()
			)
		)
		conn.commit()
		cur.execute("SELECT * FROM ptsd where rollno = {};".format(e1.get()))
		data = cur.fetchall()
		for i in data:
			Label(root, text="not found", bg="#1b1b1b", fg="white").destroy()
			f2_1 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_1.grid(row=1, column=0, sticky="EW")
			Label(f2, text="Roll no.", bg="#1b1b1b", fg="white").grid(
				row=0, column=0, sticky="EW"
			)
			Label(f2_1, text=i[0], bg="#1b1b1b", fg="white").pack()
			f2_2 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_2.grid(row=1, column=1, sticky="EW")
			Label(f2, text="Name", bg="#1b1b1b", fg="white").grid(
				row=0, column=1, sticky="EW"
			)
			Label(f2_2, text=i[1], bg="#1b1b1b", fg="white").pack()
			f2_3 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_3.grid(row=1, column=2, sticky="EW")
			Label(f2, text="Class", bg="#1b1b1b", fg="white").grid(
				row=0, column=2, sticky="EW"
			)
			Label(f2_3, text=i[2], bg="#1b1b1b", fg="white").pack()
			f2_4 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_4.grid(row=1, column=3, sticky="EW")
			Label(f2, text="D.O.B.", bg="#1b1b1b", fg="white").grid(
				row=0, column=3, sticky="EW"
			)
			Label(f2_4, text=i[3], bg="#1b1b1b", fg="white").pack()
			f2_5 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_5.grid(row=1, column=4, sticky="EW")
			Label(f2, text="Gender", bg="#1b1b1b", fg="white").grid(
				row=0, column=4, sticky="EW"
			)
			Label(f2_5, text=i[4], bg="#1b1b1b", fg="white").pack()
			f2_6 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_6.grid(row=1, column=5, sticky="EW")
			Label(f2, text="House", bg="#1b1b1b", fg="white").grid(
				row=0, column=5, sticky="EW"
			)
			Label(f2_6, text=i[5], bg="#1b1b1b", fg="white").pack()
			f2_7 = LabelFrame(f2, bg="#1b1b1b", fg="white")
			f2_7.grid(row=1, column=6, sticky="EW")
			Label(f2, text="Subject", bg="#1b1b1b", fg="white").grid(
				row=0, column=6, sticky="EW"
			)
			Label(f2_7, text=i[6], bg="#1b1b1b", fg="white").pack()

	b2 = Button(root, text="Go", command=f3_1, bg="#1b1b1b", fg="white")
	b2.grid(row=2, column=3, sticky="EW", padx=5)
	b3 = Button(root, text="Update", command=f3_2, bg="#1b1b1b", fg="white")
	b3.grid(row=4, column=3, sticky="EW", padx=5)
	b4 = Button(fb, text="refresh", width=1, command=f3, bg="#1b1b1b", fg="white")
	b4.grid(row=0, column=0, sticky="EW")

Button(root, text="Update", command=f3, bg="#1b1b1b", fg="white").grid(
	row=0, column=2, sticky="EW"
)

# DELETE
def f4():
	f0()
	Grid.rowconfigure(root, 4, weight=0)
	b1 = Button(root, text="Delete", bg="#1b1b1b", fg="grey", relief=SUNKEN, command=f4)
	b1.grid(row=0, column=3, sticky="EW")
	Label(root, bg="#1b1b1b", fg="white").grid(row=1, column=0)
	e1 = Entry(root, bg="#1b1b1b", fg="white", insertbackground="white")
	e1.grid(row=2, column=1, columnspan=2, sticky="EW")
	f2 = LabelFrame(root, bg="#1b1b1b", fg="white")
	f2.grid(row=2, column=0, sticky="EW", padx=5)
	Label(f2, text="Search:", width=1, bg="#1b1b1b", fg="white").grid(
		row=0, column=1, sticky="EW"
	)
	f1 = LabelFrame(root, text="results", bg="#1b1b1b", fg="white")
	f1.grid(row=3, column=0, columnspan=4, sticky="EW", padx=5, pady=5)
	Grid.columnconfigure(f1, 0, weight=1)
	Grid.columnconfigure(f1, 1, weight=1)
	Grid.columnconfigure(f1, 2, weight=1)
	Grid.columnconfigure(f1, 3, weight=1)
	Grid.columnconfigure(f1, 4, weight=1)
	Grid.columnconfigure(f1, 5, weight=1)
	Grid.columnconfigure(f1, 6, weight=1)
	Grid.columnconfigure(f2, 0, weight=1)
	Grid.columnconfigure(f2, 1, weight=1)
	Label(f1, bg="#1b1b1b", fg="white").grid(row=0, column=0, columnspan=8)

	def f4_1():
		if e1.get() == "/a":
			Label(
				root,
				text="WARNING! \n THIS WILL DELETE ALL ENTRIES!",
				bg="#1b1b1b",
				fg="white",
			).grid(row=3, column=1, columnspan=2)
		else:
			cur.execute("SELECT * FROM ptsd where rollno = {};".format(e1.get()))
			data = cur.fetchall()
			if cur.rowcount == 0:
				Label(root, text="not found", bg="#1b1b1b", fg="white").grid(
					row=3, column=1, columnspan=2
				)
			for i in data:
				Label(root, text="not found", bg="#1b1b1b", fg="white").destroy()
				f1_1 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_1.grid(row=1, column=0, sticky="EW")
				Label(f1, text="Roll no.", bg="#1b1b1b", fg="white").grid(
					row=0, column=0, sticky="EW"
				)
				Label(f1_1, text=i[0], bg="#1b1b1b", fg="white").pack()
				f1_2 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_2.grid(row=1, column=1, sticky="EW")
				Label(f1, text="Name", bg="#1b1b1b", fg="white").grid(
					row=0, column=1, sticky="EW"
				)
				Label(f1_2, text=i[1], bg="#1b1b1b", fg="white").pack()
				f1_3 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_3.grid(row=1, column=2, sticky="EW")
				Label(f1, text="Class", bg="#1b1b1b", fg="white").grid(
					row=0, column=2, sticky="EW"
				)
				Label(f1_3, text=i[2], bg="#1b1b1b", fg="white").pack()
				f1_4 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_4.grid(row=1, column=3, sticky="EW")
				Label(f1, text="D.O.B.", bg="#1b1b1b", fg="white").grid(
					row=0, column=3, sticky="EW"
				)
				Label(f1_4, text=i[3], bg="#1b1b1b", fg="white").pack()
				f1_5 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_5.grid(row=1, column=4, sticky="EW")
				Label(f1, text="Gender", bg="#1b1b1b", fg="white").grid(
					row=0, column=4, sticky="EW"
				)
				Label(f1_5, text=i[4], bg="#1b1b1b", fg="white").pack()
				f1_6 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_6.grid(row=1, column=5, sticky="EW")
				Label(f1, text="House", bg="#1b1b1b", fg="white").grid(
					row=0, column=5, sticky="EW"
				)
				Label(f1_6, text=i[5], bg="#1b1b1b", fg="white").pack()
				f1_7 = LabelFrame(f1, bg="#1b1b1b", fg="white")
				f1_7.grid(row=1, column=6, sticky="EW")
				Label(f1, text="Subject", bg="#1b1b1b", fg="white").grid(
					row=0, column=6, sticky="EW"
				)
				Label(f1_7, text=i[6], bg="#1b1b1b", fg="white").pack()

	def f4_2():
		if e1.get() == "/a":
			cur.execute("DELETE FROM ptsd;")
			conn.commit()
		else:
			cur.execute("DELETE FROM ptsd WHERE rollno = '{}';".format(e1.get()))
			conn.commit()
		Label(root, text="Done!", bg="#1b1b1b", fg="white").grid(
			row=4, column=0, sticky="EW", padx=5
		)

	b2 = Button(root, text="Go", command=f4_1, bg="#1b1b1b", fg="white")
	b2.grid(row=2, column=3, sticky="EW", padx=5)
	b3 = Button(f2, text="refresh", command=f4, width=1, bg="#1b1b1b", fg="white")
	b3.grid(row=0, column=0, sticky="EW")
	b4 = Button(root, text="Delete", command=f4_2, bg="#1b1b1b", fg="white")
	b4.grid(row=4, column=3, sticky="EW", padx=5)

Button(root, text="Delete", command=f4, bg="#1b1b1b", fg="white").grid(
	row=0, column=3, sticky="EW"
)

root.mainloop()