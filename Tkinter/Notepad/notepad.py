from cgitb import text
from tkinter import * 
from tkinter import filedialog
from tkinter import font
from functools import partial
from tkinter import messagebox
from datetime import datetime
import re


class Note(Tk):
    def __init__(self):
        super().__init__()
        self.title("*Untitled - Notepad")
        self.iconbitmap(r"C:\Users\Acer\3D Objects\Projects\python-workshop\Tkinter\Notepad\note.ico")
        self.geometry("720x480")
        self.minsize(360, 240)
        
        self.op_file=False
        try:
            self.selected=self.clipboard_get()
        except Exception:
            pass

        #Binders
        self.bind_all("<F5>", self.dtime)
        self.bind_all("Control-a", self.sall)
        self.bind_all("Control-A", self.sall)
        self.bind_all("<Control-s>", self.save_file)
        self.bind_all("<Control-S>", self.save_file)
        self.bind_all("<Control-Shift-s>", self.saveas_file)
        self.bind_all("<Control-Shift-S>", self.saveas_file)
        self.bind_all("<Control-n>", self.new_file)
        self.bind_all("<Control-N>", self.new_file)
        self.bind_all("<Control-o>", self.open_file)
        self.bind_all("<Control-O>", self.open_file)
        self.bind_all("<Control-p>", self.printer)
        self.bind_all("<Control-P>", self.printer)
        self.bind_all("<Control-h>", self.replacing)
        self.bind_all("<Control-H>", self.replacing)
        self.bind_all("<Control-f>", self.finding)
        self.bind_all("<Control-F>", self.finding)

        self.protocol("WM_DELETE_WINDOW", self.closing)
        self.bind_all('<Escape>', lambda e:self.close(e))

    def new_file(self, e):
        self.ta.delete(1.0, END)
        self.title("*Untitled - Notepad")
        self.fnm.config(text=r"...\Untitled.txt")
        self.op_file=False
        

    def open_file(self, e):
        text_file=filedialog.askopenfilename(initialdir=r"C:\Users\Acer\3D Objects\Projects\python-workshop\Tkinter\Notepad",
         title="Open files", filetypes=(("Text files", "*.txt"), ("HTML files", "*.html"), ("Python files", "*.py"), ("All files", "*.*")))
        if text_file:
            self.op_file=text_file
            name=text_file
            name=name.replace("C:/Users/Acer/3D Objects/Projects/python-workshop/Tkinter/Notepad/", "")
            self.fnm.config(text=f"...\{name}")
            self.title(f"{name} - Notepad")
            
            with open(text_file, "r") as f:
                textinfile=f.read()
            self.ta.delete(1.0, END)
            self.ta.insert(1.0, textinfile)

    def save_file(self, e):
        if self.op_file:
            with open(self.op_file, "w") as f:
                f.write(self.ta.get(1.0, END))
        else:
            self.saveas_file(1)


    def saveas_file(self, e):
        text_file=filedialog.asksaveasfilename(defaultextension=".*", initialdir=r"C:\Users\Acer\3D Objects\Projects\python-workshop\Tkinter\Notepad",
        title="Save file", filetypes=(("Text files", "*.txt"), ("HTML files", "*.html"), ("Python files", "*.py"), ("All files", "*.*")))
        if text_file:
            name=text_file
            name=name.replace("C:/Users/Acer/3D Objects/Projects/python-workshop/Tkinter/Notepad/", "")
            self.fnm.config(text=f"...\{name}")
            self.title(f"{name} - Notepad")
            with open(text_file, "w") as f:
                f.write(self.ta.get(1.0, END))

    def closing(self):
        if self.op_file:
            with open(self.op_file, "w") as f:
                f.write(self.ta.get(1.0, END))
            self.destroy()
        else:
            if self.ta.get(1.0, END)!="\n":
                savebox=messagebox.askyesnocancel("Quit", "Do you want to save file before quitting?")
                if savebox==True:
                    self.saveas_file()
                    self.destroy()
                elif savebox==False:
                    self.destroy()
                else:
                    pass
            else:
                self.destroy()

    def printer(self,e):
        pass
    
    def close(self, e):
        self.closing()       

    def cut(self, e):
        if e:
            self.selected= self.clipboard_get()

        if self.ta.selection_get():
            self.selected=self.ta.selection_get()
            self.ta.delete("sel.first", "sel.last")
            self.clipboard_clear()
            self.clipboard_append(self.selected)

    def copy(self, e):   
        if e:
            self.selected=self.clipboard_get() 

        if self.ta.selection_get():
            self.selected=self.ta.selection_get()
            self.clipboard_clear()
            self.clipboard_append(self.selected)
    
    def paste(self, e):
        if e:
            self.selected=self.clipboard_get()
        if self.selected:
            pos=self.ta.index(INSERT)
            self.ta.insert(pos, self.selected)

    def dele(self, e):
        if self.ta.selection_get():
            self.ta.delete("sel.first", "sel.last")

    def sall(self, e):
        self.ta.tag_add("sel", 1.0, END)

    def dtime(self, e):
        dt=datetime.now().strftime("%H:%M %d-%m-%Y")
        pos=self.ta.index(INSERT)
        self.ta.insert(pos, dt)

    def trydestroyfindbox(self):
        try:
            self.findfr.destroy()
            self.replfr.destroy()
        except Exception:
            pass

    def finding(self, e):
        self.trydestroyfindbox()
        self.findfr=Frame(self, borderwidth=2, background="black")

        self.replb=Button(self.findfr, text="⟱", background="black", foreground="white", height=1,
         activebackground="black", activeforeground="white", borderwidth=0, command=lambda: self.replacing(1))
        self.replb.grid(row=0, column=0)
        
        self.findbox=Entry(self.findfr, width=20, background="#4C4A49", foreground="white", borderwidth=0)
        self.findbox.grid(row=0, column=1) 
        self.findbox.insert(0, "Find")
        self.findbox.bind("<FocusIn>", lambda e: (self.findbox.delete(0, END)))      
        
        clearb=Button(self.findfr, text="Clear", background="black", foreground="white", height=1,
         activebackground="black", activeforeground="white", borderwidth=0, command=partial(self.findbox.delete, 0, END))
        clearb.grid(row=0, column=2)      
        
        delb=Button(self.findfr, text="[X]", background="black", foreground="red", height=1,activebackground="black", activeforeground="white", borderwidth=0, command=self.trydestroyfindbox)
        delb.grid(row=0, column=7)
        
        upb=Button(self.findfr, text="▲", background="black", foreground="white", height=1,
         activebackground="black", activeforeground="white", borderwidth=0)
        upb.grid(row=0, column=3)
        
        dob=Button(self.findfr, text="▼", background="black", foreground="white", height=1,
         activebackground="black", activeforeground="white", borderwidth=0)
        dob.grid(row=0, column=4)
        
        searchb=Button(self.findfr, text="Search", background="black", foreground="white", height=1,
         activebackground="black", activeforeground="white", borderwidth=0, command=self.searchintext)
        searchb.grid(row=0, column=5)
        
        aisehe=Label(self.findfr, text=" ", background="black")
        aisehe.grid(row=0, column=6)

        self.findfr.place(relx=0.5, rely=0.1, anchor=CENTER)

    def replacing(self, e):     
        self.finding(1)
        self.replfr=Frame(self, borderwidth=2, background="black")
        try:
            self.replb['state']=DISABLED
        except Exception:
            pass
        upb=Button(self.replfr, text="⟰", background="black", foreground="white", height=1, activebackground="black", activeforeground="white", borderwidth=0, command=lambda: [self.replfr.destroy(), self.enablebut()])
        upb.grid(row=0, column=0)
        self.replbox=Entry(self.replfr, width=20, background="#4C4A49", foreground="white", borderwidth=0)
        self.replbox.grid(row=0, column=1)
        self.replbox.insert(0, "Replace")
        self.replbox.bind("<FocusIn>", lambda e: (self.replbox.delete(0, END)))          
        clearb=Button(self.replfr, text="Clear", background="black", foreground="white", height=1, activebackground="black", activeforeground="white", borderwidth=0, command=partial(self.replbox.delete, 0, END))
        clearb.grid(row=0, column=2)
        replaceallb=Button(self.replfr, text="Replace all", background="black", foreground="white", height=1, activebackground="black", activeforeground="white", borderwidth=0)
        replaceallb.grid(row=0, column=3)
        replaceb=Button(self.replfr, text="Replace", background="black", foreground="white", height=1, activebackground="black", activeforeground="white", borderwidth=0)
        replaceb.grid(row=0, column=4)

        self.replfr.place(relx=0.5, rely=0.18, anchor=CENTER)

    def enablebut(self):
        self.replb['state']=NORMAL

    def searchintext(self):
        findvar=re.finditer(self.findbox.get(), self.ta.get(1.0, END))
        for obj in findvar:
            self.ta.tag_add("sel", float(obj.start()+1), float(obj.end()))

            # self.ta.insert(END, "\napple")
            # print(float(obj.start()+1), float(obj.end()))
            
    def menubar(self):
        self.mbar=Menu(self, background="black", foreground="white", borderwidth=0)
        self.wrap_var=BooleanVar()
        self.sbar_var=BooleanVar()
        self.m1=Menu(self.mbar, tearoff=0, background="black", foreground="white", activebackground="#2F2E2E")
        self.mbar.add_cascade(label="File", menu=self.m1)
        self.m1.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.m1.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        self.m1.add_separator()
        self.m1.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.m1.add_command(label="Save as..", command=self.saveas_file, accelerator="Ctrl+Shift+S")
        self.m1.add_separator()
        self.m1.add_command(label="Print...", command=self.fun, accelerator="Ctrl+P")
        self.m1.add_separator()
        self.m1.add_command(label="Exit", command=self.closing)

        self.m2=Menu(self.mbar, tearoff=0, background="black", foreground="white", activebackground="#2F2E2E")
        self.mbar.add_cascade(label="Edit", menu=self.m2)
        self.m2.add_command(label="Undo", command=self.ta.edit_undo, accelerator="Ctrl+Z")
        self.m2.add_command(label="Redo", command=self.ta.edit_redo, accelerator="Ctrl+Y")
        self.m2.add_separator()
        self.m2.add_command(label="Cut", command=lambda: self.cut(1), accelerator="Ctrl+X")
        self.m2.add_command(label="Copy", command=lambda: self.copy(1), accelerator="Ctrl+C")
        self.m2.add_command(label="Paste", command=lambda: self.paste(1), accelerator="Ctrl+V")
        self.m2.add_command(label="Delete", command=self.dele, accelerator="Del")
        self.m2.add_separator()
        self.m2.add_command(label="Find..", command=lambda: self.finding(1), accelerator="Ctrl+F")
        self.m2.add_command(label="Replace..", command=lambda:[self.finding(1), self.replacing(1)], accelerator="Ctrl+H")
        self.m2.add_separator()
        self.m2.add_command(label="Select all..", command=self.sall, accelerator="Ctrl+A")
        self.m2.add_command(label="Time/Date", command=self.dtime, accelerator="F5")

        self.m5=Menu(self.mbar, tearoff=0, background="black", foreground="white", activebackground="#2F2E2E")
        self.mbar.add_cascade(label="Format", menu=self.m5)
        self.m5.add_checkbutton(label="Word Wrap", onvalue=1, offvalue=0, variable=self.wrap_var)
        self.m5.add_separator()
        self.m5.add_command(label="Font...", command=self.fun)

        self.m3=Menu(self.mbar, tearoff=0, background="black", foreground="white", activebackground="#2F2E2E")
        self.mbar.add_cascade(label="View", menu=self.m3)
        self.zm=Menu(self.m3, tearoff=0, background="black", foreground="white", activebackground="#2F2E2E")
        self.m3.add_cascade(label="Zoom", menu=self.zm)
        self.zm.add_command(label="Zoom In", command=self.fun)
        self.zm.add_command(label="Zoom Out", command=self.fun)
        self.zm.add_command(label="Restore default Zoom", command=self.fun)
        self.m3.add_separator()
        self.m3.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0, variable=self.sbar_var)

        self.m4=Menu(self.mbar, tearoff=0, background="black", foreground="white", activebackground="#2F2E2E")
        self.mbar.add_cascade(label="Help", menu=self.m4)
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
        
        self.ta=Text(self.mf, pady=5, font=("lucida Console", 13), selectforeground="blue", undo=True,
         selectbackground="grey", wrap="none", background="#2F2E2E", foreground="white", insertbackground="white")
        self.scrolly=Scrollbar(self.mf, orient=VERTICAL, command=self.ta.yview)
        self.scrollx=Scrollbar(self.mf, orient=HORIZONTAL, command=self.ta.xview)
        self.scrollx.pack(fill=X, side=BOTTOM)
        self.scrolly.pack(fill=Y, side=RIGHT)
        self.ta.pack(side=LEFT, fill=BOTH, expand=True)

        self.ta.config(xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)
        self.ta.bind_all("<MouseWheel>", lambda e: self.ta.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.bind_all("Shift-MouseWheel", lambda e: self.ta.xview_scroll(int(-1*(e.delta/120)), "units"))

    def statebar(self, lv, colv, zv):
        self.sbar=Frame(self)
        self.fnm=Label(self.sbar, text=r"...\Untitled.txt")
        self.fnm.pack(side="left", ipadx=10)
        self.szo=Label(self.sbar, text=f"{zv}%")
        self.szo.pack(side="right", ipadx=40)
        self.slc=Label(self.sbar, text=f"Ln {lv}, Col {colv}")
        self.slc.pack(side="right", ipadx=40)
        self.sbar.update()
        self.sbar.pack(fill=X, side=BOTTOM, ipady=5)

if __name__=="__main__":
    npad=Note()
    npad.tarea()
    npad.menubar()
    npad.wrap_var.set(0)
    npad.sbar_var.set(1)
    npad.statebar(0, 0, 100)
    npad.mainloop()