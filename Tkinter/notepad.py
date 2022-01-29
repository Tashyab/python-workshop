from operator import truediv
from tkinter import * 
from functools import partial
from turtle import left, right

from click import command

class Note(Tk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.iconbitmap(r"C:\Users\Acer\3D Objects\Projects\python-workshop\Tkinter\note.ico")
        self.geometry("720x480")
        self.minsize(360, 240)

    def menubar(self):
        self.mbar=Menu(self)

        self.m1=Menu(self.mbar, tearoff=0)
        self.m1.add_cascade(label="File", menu=self.m1)
        self.m1.add_command(label="New", command=self.fun)
        self.m1.add_command(label="Open...", command=self.fun)
        self.m1.add_separator()
        self.m1.add_command(label="Save", command=self.fun)
        self.m1.add_command(label="Save as..", command=self.fun)
        self.m1.add_separator()
        self.m1.add_command(label="Print...", command=self.fun)
        self.m1.add_separator()
        self.m1.add_command(label="Exit", command=self.fun)

        self.m2=Menu(self.mbar, tearoff=0)
        self.m2.add_cascade(label="Edit", menu=self.m2)
        self.m2.add_command(label="Undo", command=self.fun)
        self.m2.add_command(label="Redo", command=self.fun)
        self.m2.add_separator()
        self.m2.add_command(label="Cut", command=self.fun)
        self.m2.add_command(label="Copy", command=self.fun)
        self.m2.add_command(label="Paste", command=self.fun)
        self.m2.add_command(label="Delete", command=self.fun)
        self.m2.add_separator()
        self.m2.add_command(label="Find..", command=self.fun)
        self.m2.add_command(label="Replace..", command=self.fun)
        self.m2.add_separator()
        self.m2.add_command(label="Select all..", command=self.fun)
        self.m2.add_command(label="Time/Date", command=self.fun)

        self.m3=Menu(self.mbar, tearoff=0)
        self.m3.add_cascade(label="View", menu=self.m3)
        self.m3.add_command(label="Zoom")
        self.m3.add_command(label="Status Bar")

        self.m4=Menu(self.mbar, tearoff=0)
        self.m4.add_cascade(label="Help", command=self.m4)
        self.m4.add_command(label="View Help", command=self.fun)
        self.m4.add_command(label="Send Feedback", command=self.fun)
        self.m4.add_separator()
        self.m4.add_command(label="About Notepad", command=self.fun)

        self.config(menu=self.mbar)

    def fun(self):
        pass

    def tarea(self):
        self.mf=Frame(self)
        self.mf.pack(fill=BOTH, expand=True)
        
        self.ta=Text(self.mf, font=("lucida Console", 13), selectforeground="blue", undo=True, selectbackground="grey", wrap=None)
        self.scrolly=Scrollbar(self.mf, orient=VERTICAL, command=self.ta.yview)
        self.scrollx=Scrollbar(self.mf, orient=HORIZONTAL, command=self.ta.xview)
        self.scrollx.pack(fill=X, side=BOTTOM)
        self.scrolly.pack(fill=Y, side=RIGHT)
        self.ta.pack(side=LEFT, fill=BOTH, expand=True)

        self.ta.config(xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)
        self.ta.bind_all("<MouseWheel>", lambda e: self.ta.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.bind_all("Shift-MouseWheel", lambda e: self.ta.xview_scroll(int(-1*(e.delta/120)), "units"))

        


if __name__=="__main__":
    npad=Note()
    npad.menubar()
    npad.tarea()
    npad.mainloop()