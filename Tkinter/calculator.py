import math
import time
from tkinter import *
from functools import partial

class Calc(Tk):
    def __init__(self):
        super().__init__()
        sw=self.winfo_screenwidth()
        self.title("Calculator")
        self.iconbitmap(r"C:\Users\Acer\3D Objects\Projects\python-workshop\Tkinter\calcr.ico")
        self.geometry(f"700x238+{(int)(sw/2)-280}+200")
        self.minsize(700, 238)
        self.maxsize(700, 238)
        self.config(bg="black")

    def create_entry(self, w, bw, rel, row, col, f):
        self.en=Entry(self, width=w, borderwidth=bw, relief=rel, font=f, background="black", foreground="white")
        self.en.grid(row=row, column=col, columnspan=5, padx=10, pady=0)
        self.en.insert(0, 0)

    def create_button(self, name, fun, rel, ft, row, col, bgc, abc):
        self.button=Button(text=name, command=fun, relief=rel, font=ft, bg=bgc, fg="white", activeforeground="white", activebackground=abc)
        self.button.grid(row=row, column=col, sticky=E+W)

    def error(self, e):
        self.en.insert(0, f"{e}")
        self.en.update()
        time.sleep(1)
        self.en.delete(0, END)
        self.en.insert(0, "0")

    def show(self, d):
        n=self.en.get()
        l=len(n)   
        if d==0:
            if n!="0":
                self.en.insert(l, f"{d}")
        elif d=="." and (d not in n):
            if n=="":
                self.en.insert(l, f"{0}{d}")
            else:
                self.en.insert(l, f"{d}")
        elif (d!=".") and (d!=0):
            if(n!="0"):
                self.en.insert(l, f"{d}")
            else:
                self.en.delete(l-1, END)
                self.en.insert(l-1, f"{d}")
    
    def change_sign(self):
        n=self.en.get()       
        if float(n)<0:
            n=abs(float(n))
        else:
            n=f"-{n}"
        self.en.delete(0, END)
        self.en.insert(0, f"{self.val_int(n)}")

    def back(self):
        n=self.en.get()
        l=len(n)
        if l>0:
            if n[l-1].isdigit() or n[l-1]==".":
                self.en.delete(l-1, END)
            elif n[l-1]==')':
                if n[l-2]=='(':
                    self.en.delete(0, END)
                else:
                    self.en.delete(l-2, l-1)
            else:
                self.en.delete(0, END)
                self.en.insert(0, "0")
        if self.en.get()=="" or self.en.get()=="-":
            self.en.delete(0, END)
            self.en.insert(0, "0")

    def ac(self):
        self.en.delete(0, END)
        self.en.insert(0, "0")

    def extn(self):
        global nx
        nx=self.en.get()

    def getfn(self):
        global fn
        fn=self.en.get()
        if fn=="":
            fn=nx
        else:
            self.extn()
        self.en.delete(0, END)

    def takef(self, op):
        global v
        v=op
        self.getfn()

    def val_int(self, k):
        k=float(k)
        if k==int(k):
            k=int(k)
        return k

    def per(self):
        nu=float(self.en.get())
        nu=nu/100
        self.en.delete(0, END)
        self.en.insert(0, f"{self.val_int(nu)}")

    def eq(self):
        sn=self.en.get()
        global fn
        
        try:
            if v=="+":
                self.en.delete(0, END)
                sum=(float)(fn)+(float)(sn)
                self.en.insert(0, f"{self.val_int(sum)}")

            elif(v=="-"):
                self.en.delete(0, END)
                diff=(float)(fn)-(float)(sn)
                self.en.insert(0, f"{self.val_int(diff)}")

            elif(v=="x"):
                self.en.delete(0, END)
                pro=(float)(fn)*(float)(sn)
                self.en.insert(0, f"{self.val_int(pro)}")

            elif(v=="/"):
                self.en.delete(0, END)
                try:
                    di=(float)(fn)/(float)(sn)
                    self.en.insert(0, f"{self.val_int(di)}") 
                except Exception:
                    self.error("Can't divide by 0")
        except Exception:
            pass

    def fun(self, f):
        global v
        n=self.en.get()
        if n=="":
            n=nx
        self.en.delete(0, END)
        if f=="tan":
            n=float(n)
            n=math.tan(math.radians(n))
            self.en.insert(0, f"{self.val_int(n)}")
            
        elif f=="sin":
            n=float(n)
            n=math.sin(math.radians(n))
            self.en.insert(0, f"{self.val_int(n)}")

        elif f=="cos":
            n=float(n)
            n=math.cos(math.radians(n))
            self.en.insert(0, f"{self.val_int(n)}")

        elif f=="log":
            n=float(n)
            if(n>0):
                n=math.log10(n)
                self.en.insert(0, f"{self.val_int(n)}")
            else:
                self.error("Invalid input")                

        elif f=="√":
            n=float(n)
            if(n>=0):
                n=math.sqrt(n)
                self.en.insert(0, f"{self.val_int(n)}")
            else:
                self.error("Invalid input")


if __name__=="__main__":
    win=Calc()

    entry=win.create_entry(60, 6, "solid", 0, 0, "Helvetica")

    row=0
    col=3
    for i in reversed(range(1, 10)):
        if(i<=3):
            row=3
        elif(i<=6):
            row=2
        else:
            row=1
        button=win.create_button(i, partial(win.show, i), "raised", "bold", row, col, "#383838", "#212121")
        if(col==1):
            col=3
        else:
            col-=1
            
    bsign=win.create_button("±", win.change_sign, "raised", "bold", 4, 1, "#383838", "#212121")
    b0=win.create_button("0", partial(win.show, 0), "raised", "bold", 4, 2, "#383838", "#212121")
    bdec=win.create_button(".", partial(win.show, "."), "raised", "bold", 4, 3, "#383838", "#212121")

    bdel=win.create_button("⌫", win.back, "raised", "bold", 1, 0, "#212121", "#212121")
    bac=win.create_button("AC", win.ac, "raised", "bold", 1, 4, "#212121", "#212121")

    bmul=win.create_button("x", partial(win.takef, "x"), "raised", "bold", 2, 0, "#212121", "#383838")
    bdiv=win.create_button("/", partial(win.takef, "/"), "raised", "bold", 2, 4, "#212121", "#383838")

    bplus=win.create_button("+", partial(win.takef, "+"), "raised", "bold", 3, 0, "#212121", "#383838")
    bmin=win.create_button("-", partial(win.takef, "-"), "raised", "bold", 3, 4, "#212121", "#383838")

    bper=win.create_button("%", win.per, "raised", "bold", 4, 0, "#212121", "#383838")
    broot=win.create_button("√", partial(win.fun, "√"), "raised", "bold", 4, 4, "#212121", "#383838")

    bsin=win.create_button("sin", partial(win.fun, "sin"), "raised", "bold", 5, 0, "#212121", "#383838")
    bcos=win.create_button("cos", partial(win.fun, "cos"), "raised", "bold", 5, 1, "#212121", "#383838")
    btan=win.create_button("tan", partial(win.fun, "tan"), "raised", "bold", 5, 2, "#212121", "#383838")
    blog=win.create_button("log", partial(win.fun, "log"), "raised", "bold", 5, 3, "#212121", "#383838")
    beq=win.create_button("=", win.eq, "raised", "bold", 5, 4, "#1d3d81", "#2a56b7")
        
    win.mainloop()