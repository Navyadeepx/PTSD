import os
import pickle
from tkinter import *
from ttkbootstrap import *

root = Window(themename='darkly')
root.geometry("600x400")
root.title("P.T.S.D. V4.5")
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)

a1 = Label(root, text='"Choose any tab to continue"')
a1.grid(row=4, column=0, sticky="EW", columnspan=4)


def f0():
    for Widget in root.winfo_children():
        Widget.destroy()
    Button(root, text="Enter", command=f1).grid(row=0, column=0, sticky="EW")
    Button(root, text="Search", command=f2).grid(row=0, column=1, sticky="EW")
    Button(root, text="Update", command=f3).grid(row=0, column=2, sticky="EW")
    Button(root, text="Delete", command=f4).grid(row=0, column=3, sticky="EW")


def f1():
    f0()
    Grid.rowconfigure(root, 4, weight=0)
    b1 = Button(root, text="Enter",command=f1)
    b1.grid(row=0, column=0, sticky="EW")
    Label(root).grid(row=11, column=0, columnspan=4)
    f = LabelFrame(root, text="Entered data")
    f.grid(row=12, column=0, rowspan=8, columnspan=4, sticky="EWNS", padx=5, pady=5)
    Grid.columnconfigure(f, 0, weight=1)
    Grid.columnconfigure(f, 1, weight=1)
    Grid.columnconfigure(f, 2, weight=1)
    Grid.columnconfigure(f, 3, weight=1)
    Grid.columnconfigure(f, 4, weight=1)
    Grid.columnconfigure(f, 5, weight=1)
    Grid.columnconfigure(f, 6, weight=1)
    Label(f).grid(row=0, column=0, columnspan=8)
    Label(root, text="").grid(row=1, column=0)
    Label(root, text="Roll no.: ").grid(row=2, column=0)
    Label(root, text="Name: ").grid(row=3, column=0)
    Label(root, text="Class: ").grid(row=4, column=0)
    Label(root, text="D.O.B.: ").grid(row=5, column=0)
    Label(root, text="Gender: ").grid(row=6, column=0)
    Label(root, text="House: ").grid(row=7, column=0)
    Label(root, text="Subject: ").grid(row=8, column=0)
    e1 = Entry(root)
    e1.grid(row=2, column=1, columnspan=2, sticky="EW")
    e2 = Entry(root)
    e2.grid(row=3, column=1, columnspan=2, sticky="EW")
    e3 = Entry(root)
    e3.grid(row=4, column=1, columnspan=2, sticky="EW")
    e4 = Entry(root)
    e4.grid(row=5, column=1, columnspan=2, sticky="EW")
    e5 = Entry(root)
    e5.grid(row=6, column=1, columnspan=2, sticky="EW")
    e6 = Entry(root)
    e6.grid(row=7, column=1, columnspan=2, sticky="EW")
    e7 = Entry(root)
    e7.grid(row=8, column=1, columnspan=2, sticky="EW")

    def f1_1():
        stufile = open("stu.bin", "ab")
        stu = {}
        stu["roll no"] = e1.get()
        stu["name"] = e2.get()
        stu["class"] = e3.get()
        stu["d.o.b"] = e4.get()
        stu["gender"] = e5.get()
        stu["house"] = e6.get()
        stu["subject"] = e7.get()
        pickle.dump(stu, stufile)
        f1_1 = LabelFrame(f)
        f1_1.grid(row=1, column=0, sticky="EW")
        Label(f, text="Roll no.").grid(row=0, column=0, sticky="EW")
        Label(f1_1, text=stu["roll no"]).pack()
        f1_2 = LabelFrame(f)
        f1_2.grid(row=1, column=1, sticky="EW")
        Label(f, text="Name").grid(row=0, column=1, sticky="EW")
        Label(f1_2, text=stu["name"]).pack()
        f1_3 = LabelFrame(f)
        f1_3.grid(row=1, column=2, sticky="EW")
        Label(f, text="Class").grid(row=0, column=2, sticky="EW")
        Label(f1_3, text=stu["class"]).pack()
        f1_4 = LabelFrame(f)
        f1_4.grid(row=1, column=3, sticky="EW")
        Label(f, text="D.O.B.").grid(row=0, column=3, sticky="EW")
        Label(f1_4, text=stu["d.o.b"]).pack()
        f1_5 = LabelFrame(f)
        f1_5.grid(row=1, column=4, sticky="EW")
        Label(f, text="Gender").grid(row=0, column=4, sticky="EW")
        Label(f1_5, text=stu["gender"]).pack()
        f1_6 = LabelFrame(f)
        f1_6.grid(row=1, column=5, sticky="EW")
        Label(f, text="House").grid(row=0, column=5, sticky="EW")
        Label(f1_6, text=stu["house"]).pack()
        f1_7 = LabelFrame(f)
        f1_7.grid(row=1, column=6, sticky="EW")
        Label(f, text="Subject").grid(row=0, column=6, sticky="EW")
        Label(f1_7, text=stu["subject"]).pack()
        stufile.close()

    b2 = Button(root, text="Save", width=10, command=f1_1)
    b2.grid(row=10, column=2, sticky="E")
    b3 = Button(root, text="refresh", width=10, command=f1)
    b3.grid(row=10, column=1, sticky="W")


Button(root, text="Enter", command=f1).grid(row=0, column=0, sticky="EW")


def f2():
    f0()
    Grid.rowconfigure(root, 4, weight=1)
    b1 = Button(root, text="Search",command=f2)
    b1.grid(row=0, column=1, sticky="EW")
    f1 = LabelFrame(root, text="results", padx=5)
    f1.grid(row=4, column=0, rowspan=8, columnspan=4, sticky="EWNS", padx=5, pady=5)
    Grid.columnconfigure(f1, 0, weight=1)
    Grid.columnconfigure(f1, 1, weight=1)
    Grid.columnconfigure(f1, 2, weight=1)
    Grid.columnconfigure(f1, 3, weight=1)
    Grid.columnconfigure(f1, 4, weight=1)
    Grid.columnconfigure(f1, 5, weight=1)
    Grid.columnconfigure(f1, 6, weight=1)
    Label(root, text="").grid(row=1, column=0)
    c1 = StringVar()
    c1.set("roll no")
    c2 = OptionMenu(
        root, c1, "roll no", "name", "class", "d.o.b", "gender", "house", "subject"
    )
    c2.grid(
        row=2,
        column=0,
        sticky="EW",
        padx=5,
    )
    e1 = Entry(root)
    e1.grid(row=2, column=1, columnspan=2, sticky="EW")

    def f2_1():
        stu = {}
        f1_1 = LabelFrame(f1)
        f1_1.grid(row=1, column=0, sticky="EW")
        Label(f1, text="Roll no.").grid(row=0, column=0, sticky="EW")
        f1_2 = LabelFrame(f1)
        f1_2.grid(row=1, column=1, sticky="EW")
        Label(f1, text="Name").grid(row=0, column=1, sticky="EW")
        f1_3 = LabelFrame(f1)
        f1_3.grid(row=1, column=2, sticky="EW")
        Label(f1, text="Class").grid(row=0, column=2, sticky="EW")
        f1_4 = LabelFrame(f1)
        f1_4.grid(row=1, column=3, sticky="EW")
        Label(f1, text="D.O.B.").grid(row=0, column=3, sticky="EW")
        f1_5 = LabelFrame(f1)
        f1_5.grid(row=1, column=4, sticky="EW")
        Label(f1, text="Gender").grid(row=0, column=4, sticky="EW")
        f1_6 = LabelFrame(f1)
        f1_6.grid(row=1, column=5, sticky="EW")
        Label(f1, text="House").grid(row=0, column=5, sticky="EW")
        f1_7 = LabelFrame(f1)
        f1_7.grid(row=1, column=6, sticky="EW")
        Label(f1, text="Subject").grid(row=0, column=6, sticky="EW")
        found = False
        param = c1.get()
        entry = str(e1.get())
        if entry == "showall":
            fin = open("stu.bin", "rb")
            try:
                while True:
                    stu = pickle.load(fin)
                    Label(f1_1, text=stu["roll no"]).pack()
                    Label(f1_2, text=stu["name"]).pack()
                    Label(f1_3, text=stu["class"]).pack()
                    Label(f1_4, text=stu["d.o.b"]).pack()
                    Label(f1_5, text=stu["gender"]).pack()
                    Label(f1_6, text=stu["house"]).pack()
                    Label(f1_7, text=stu["subject"]).pack()
            except EOFError:
                fin.close()
        else:
            fin = open("stu.bin", "rb")
            try:
                while True:
                    stu = pickle.load(fin)
                    if stu[param] == entry:
                        Label(f1_1, text=stu["roll no"]).pack()
                        Label(f1_2, text=stu["name"]).pack()
                        Label(f1_3, text=stu["class"]).pack()
                        Label(f1_4, text=stu["d.o.b"]).pack()
                        Label(f1_5, text=stu["gender"]).pack()
                        Label(f1_6, text=stu["house"]).pack()
                        Label(f1_7, text=stu["subject"]).pack()
                        found = True
            except EOFError:
                if found == False:
                    l1 = Label(f1, text="given entry not found")
                    l1.grid(row=1, column=0, sticky="EW", columnspan=7)
                else:
                    fin.close()

    b2 = Button(root, text="Go", command=f2_1)
    b2.grid(row=2, column=3, sticky="EW", padx=5)
    b3 = Button(root, text="refresh", command=f2)
    b3.grid(row=90, column=3, sticky="EW", padx=5, pady=5)


Button(root, text="Search", command=f2).grid(row=0, column=1, sticky="EW")


def f3():
    f0()
    Grid.rowconfigure(root, 4, weight=0)
    b1 = Button(root, text="Update",command=f3)
    n = "navyadeep"
    b1.grid(row=0, column=2, sticky="EW")
    f1 = LabelFrame(root, text="results")
    f1.grid(row=3, column=0, columnspan=4, sticky="EW", padx=5, pady=5)
    Grid.columnconfigure(f1, 0, weight=1)
    Grid.columnconfigure(f1, 1, weight=1)
    Grid.columnconfigure(f1, 2, weight=1)
    Grid.columnconfigure(f1, 3, weight=1)
    Grid.columnconfigure(f1, 4, weight=1)
    Grid.columnconfigure(f1, 5, weight=1)
    Grid.columnconfigure(f1, 6, weight=1)
    Label(f1).grid(row=0, column=0, columnspan=8)
    f2 = LabelFrame(root, text="results")
    f2.grid(row=5, column=0, columnspan=4, sticky="EW", padx=5, pady=5)
    Grid.columnconfigure(f2, 0, weight=1)
    Grid.columnconfigure(f2, 1, weight=1)
    Grid.columnconfigure(f2, 2, weight=1)
    Grid.columnconfigure(f2, 3, weight=1)
    Grid.columnconfigure(f2, 4, weight=1)
    Grid.columnconfigure(f2, 5, weight=1)
    Grid.columnconfigure(f2, 6, weight=1)
    Label(f2).grid(row=0, column=0, columnspan=8)
    Label(root, text="").grid(row=1, column=0)
    fb = LabelFrame(root)
    fb.grid(row=2, column=0, sticky="EW", padx=5)
    Grid.columnconfigure(fb, 0, weight=1)
    Grid.columnconfigure(fb, 1, weight=1)
    Label(fb, text="Search:", width=1).grid(row=0, column=1, sticky="Ew")
    e1 = Entry(root)
    e1.grid(row=2, column=1, columnspan=2, sticky="EW")

    def f3_1():
        stu = {}
        found = False
        fin = open("stu.bin", "rb")
        entry = e1.get()
        try:
            while True:
                stu = pickle.load(fin)
                if stu["roll no"] == entry:
                    Label(root, text="not found").destroy()
                    f1_1 = LabelFrame(f1)
                    f1_1.grid(row=1, column=0, sticky="EW")
                    Label(f1, text="Roll no.").grid(row=0, column=0, sticky="EW")
                    Label(f1_1, text=stu["roll no"]).pack()
                    f1_2 = LabelFrame(f1)
                    f1_2.grid(row=1, column=1, sticky="EW")
                    Label(f1, text="Name").grid(row=0, column=1, sticky="EW")
                    Label(f1_2, text=stu["name"]).pack()
                    f1_3 = LabelFrame(f1)
                    f1_3.grid(row=1, column=2, sticky="EW")
                    Label(f1, text="Class").grid(row=0, column=2, sticky="EW")
                    Label(f1_3, text=stu["class"]).pack()
                    f1_4 = LabelFrame(f1)
                    f1_4.grid(row=1, column=3, sticky="EW")
                    Label(f1, text="D.O.B.").grid(row=0, column=3, sticky="EW")
                    Label(f1_4, text=stu["d.o.b"]).pack()
                    f1_5 = LabelFrame(f1)
                    f1_5.grid(row=1, column=4, sticky="EW")
                    Label(f1, text="Gender").grid(row=0, column=4, sticky="EW")
                    Label(f1_5, text=stu["gender"]).pack()
                    f1_6 = LabelFrame(f1)
                    f1_6.grid(row=1, column=5, sticky="EW")
                    Label(f1, text="House").grid(row=0, column=5, sticky="EW")
                    Label(f1_6, text=stu["house"]).pack()
                    f1_7 = LabelFrame(f1)
                    f1_7.grid(row=1, column=6, sticky="EW")
                    Label(f1, text="Subject").grid(row=0, column=6, sticky="EW")
                    Label(f1_7, text=stu["subject"]).pack()
                    found = True
        except EOFError:
            if found == False:
                Label(root, text="not found").grid(row=3, column=1, columnspan=2)
            else:
                fin.close()

    c1 = StringVar()
    c1.set("name")
    c2 = OptionMenu(root, c1, "name", "class", "d.o.b", "gender", "house", "subject")
    c2.grid(
        row=4,
        column=0,
        sticky="EW",
    )
    e2 = Entry(root)
    e2.grid(row=4, column=1, columnspan=2, sticky="EW", padx=5)

    def f3_2():
        x, y, z = e1.get(), c1.get(), e2.get()
        stu = {}
        stufile = open("stu.bin", "rb")
        try:
            bin = open("temp.tmp", "ab")
            while True:
                stu = pickle.load(stufile)
                if stu["roll no"] == x:
                    stu[y] = z
                    Label(root, text="not found").destroy()
                    f1_1 = LabelFrame(f2)
                    f1_1.grid(row=1, column=0, sticky="EW")
                    Label(f2, text="Roll no.").grid(row=0, column=0, sticky="EW")
                    Label(f1_1, text=stu["roll no"]).pack()
                    f1_2 = LabelFrame(f2)
                    f1_2.grid(row=1, column=1, sticky="EW")
                    Label(f2, text="Name").grid(row=0, column=1, sticky="EW")
                    Label(f1_2, text=stu["name"]).pack()
                    f1_3 = LabelFrame(f2)
                    f1_3.grid(row=1, column=2, sticky="EW")
                    Label(f2, text="Class").grid(row=0, column=2, sticky="EW")
                    Label(f1_3, text=stu["class"]).pack()
                    f1_4 = LabelFrame(f2)
                    f1_4.grid(row=1, column=3, sticky="EW")
                    Label(f2, text="D.O.B.").grid(row=0, column=3, sticky="EW")
                    Label(f1_4, text=stu["d.o.b"]).pack()
                    f1_5 = LabelFrame(f2)
                    f1_5.grid(row=1, column=4, sticky="EW")
                    Label(f2, text="Gender").grid(row=0, column=4, sticky="EW")
                    Label(f1_5, text=stu["gender"]).pack()
                    f1_6 = LabelFrame(f2)
                    f1_6.grid(row=1, column=5, sticky="EW")
                    Label(f2, text="House").grid(row=0, column=5, sticky="EW")
                    Label(f1_6, text=stu["house"]).pack()
                    f1_7 = LabelFrame(f2)
                    f1_7.grid(row=1, column=6, sticky="EW")
                    Label(f2, text="Subject").grid(row=0, column=6, sticky="EW")
                    Label(f1_7, text=stu["subject"]).pack()
                pickle.dump(stu, bin)
        except EOFError:
            stufile.close()
        bin.close()
        os.remove("stu.bin")
        os.rename("temp.tmp", "stu.bin")

    b2 = Button(root, text="Go", command=f3_1)
    b2.grid(row=2, column=3, sticky="EW", padx=5)
    b3 = Button(root, text="Update", command=f3_2)
    b3.grid(row=4, column=3, sticky="EW", padx=5)
    b4 = Button(fb, text="refresh", width=1, command=f3)
    b4.grid(row=0, column=0, sticky="EW")
    Label(root, text="").grid(row=5, column=0)


Button(root, text="Update", command=f3).grid(row=0, column=2, sticky="EW")


def f4():
    f0()
    Grid.rowconfigure(root, 4, weight=0)
    b1 = Button(root, text="Delete",command=f4)
    b1.grid(row=0, column=3, sticky="EW")
    Label(root, text="").grid(row=1, column=0)
    e1 = Entry(root)
    e1.grid(row=2, column=1, columnspan=2, sticky="EW")
    f2 = LabelFrame(root)
    f2.grid(row=2, column=0, sticky="EW", padx=5)
    Label(f2, text="Search:", width=1).grid(row=0, column=1, sticky="EW")
    f1 = LabelFrame(root, text="results")
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
    Label(f1).grid(row=0, column=0, columnspan=8)

    def f4_1():
        stu = {}
        found = False
        fin = open("stu.bin", "rb")
        entry = e1.get()
        try:
            while True:
                stu = pickle.load(fin)
                if stu["roll no"] == entry:
                    Label(root, text="not found").destroy()
                    f1_1 = LabelFrame(f1)
                    f1_1.grid(row=1, column=0, sticky="EW")
                    Label(f1, text="Roll no.").grid(row=0, column=0, sticky="EW")
                    Label(f1_1, text=stu["roll no"]).pack()
                    f1_2 = LabelFrame(f1)
                    f1_2.grid(row=1, column=1, sticky="EW")
                    Label(f1, text="Name").grid(row=0, column=1, sticky="EW")
                    Label(f1_2, text=stu["name"]).pack()
                    f1_3 = LabelFrame(f1)
                    f1_3.grid(row=1, column=2, sticky="EW")
                    Label(f1, text="Class").grid(row=0, column=2, sticky="EW")
                    Label(f1_3, text=stu["class"]).pack()
                    f1_4 = LabelFrame(f1)
                    f1_4.grid(row=1, column=3, sticky="EW")
                    Label(f1, text="D.O.B.").grid(row=0, column=3, sticky="EW")
                    Label(f1_4, text=stu["d.o.b"]).pack()
                    f1_5 = LabelFrame(f1)
                    f1_5.grid(row=1, column=4, sticky="EW")
                    Label(f1, text="Gender").grid(row=0, column=4, sticky="EW")
                    Label(f1_5, text=stu["gender"]).pack()
                    f1_6 = LabelFrame(f1)
                    f1_6.grid(row=1, column=5, sticky="EW")
                    Label(f1, text="House").grid(row=0, column=5, sticky="EW")
                    Label(f1_6, text=stu["house"]).pack()
                    f1_7 = LabelFrame(f1)
                    f1_7.grid(row=1, column=6, sticky="EW")
                    Label(f1, text="Subject").grid(row=0, column=6, sticky="EW")
                    Label(f1_7, text=stu["subject"]).pack()
                    found = True
        except EOFError:
            if found == False:
                Label(root, text="not found").grid(row=3, column=1, columnspan=2)
            else:
                fin.close()

    def f4_2():
        x = e1.get()
        stu = {}
        stufile = open("stu.bin", "rb")
        try:
            bin = open("temp.tmp", "ab")
            while True:
                stu = pickle.load(stufile)
                if stu["roll no"] == x:
                    stu.clear()
                else:
                    pickle.dump(stu, bin)
        except EOFError:
            stufile.close()
        bin.close()
        os.remove("stu.bin")
        os.rename("temp.tmp", "stu.bin")

    b2 = Button(root, text="Go", command=f4_1)
    b2.grid(row=2, column=3, sticky="EW", padx=5)
    b3 = Button(f2, text="refresh", command=f4, width=1)
    b3.grid(row=0, column=0, sticky="EW")
    b4 = Button(root, text="Delete", command=f4_2)
    b4.grid(row=4, column=3, sticky="EW", padx=5)


Button(root, text="Delete", command=f4).grid(row=0, column=3, sticky="EW")
root.mainloop()
