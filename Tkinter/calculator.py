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
        self.geometry(f"700x238+{(int)(sw/2)-200}+200")
        self.minsize(700, 238)
        self.maxsize(700, 238)

    def create_entry(self, w, bw, rel, row, col, f):
        self.en=Entry(self, width=w, borderwidth=bw, relief=rel, font=f)
        self.en.grid(row=row, column=col, columnspan=5, padx=10, pady=0)
        # self.en.insert(0, 0)

    def create_button(self, name, fun, rel, ft, row, col):
        self.button=Button(text=name, command=fun, relief=rel, font=ft)
        self.button.grid(row=row, column=col, sticky=E+W)
    
    def error(self, e):
        self.en.insert(0, f"{e}")

    def show(self, d):
        n=self.en.get()
        l=len(n)   
        if n!="" and (n[0].isalpha() or n[0]=="√"):
            if n[0].isalpha():
                k=4
            else:
                k=2
            if d==0:
                if n[k]=="0" and n[k+1]!=".":
                    pass
                else:
                    self.en.insert(l-1, f"{d}")
            elif d=="." and (d not in n):
                if n=="":
                    self.en.insert(l-1, f"{0}{d}")
                else:
                    self.en.insert(l-1, f"{d}")
            elif (d!=".") and (d!=0):
                if n[k]=="0" and n[k+1]!=".":
                    self.en.delete(l-2, l-1)
                    self.en.insert(l-2, f"{d}")
                else:
                    self.en.insert(l-1, f"{d}")
        else:
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
        n1=""
        st=""
        if(n==""):
            self.en.insert(0, "-")
        elif(n=="-"):
            self.en.delete(0, END)
        else:
            for ch in n:
                if ch.isdigit():
                    n1=n1+ch              
            if float(n1)<0:
                n1=abs(float(n1))
                n1=self.val_int(n1)
            else:
                n1=f"-{n1}"
            for ch in n:
                if ch.isalpha() or ch=='√':
                    st=st+ch
            self.en.delete(0, END)
            self.en.insert(0, f"{st}{self.val_int(n1)}")

    def back(self):
        n=self.en.get()
        l=len(n)
        if n[l-1].isdigit():
            self.en.delete(l-1, END)
        elif n[l-1]==')':
            if n[l-2]=='(':
                self.en.delete(0, END)
            else:
                self.en.delete(l-2, l-1)
        else:
            self.en.delete(0, END)

    def ac(self):
        self.en.delete(0, END)

    def getfn(self):
        global fn
        fn=self.en.get()
        st=""
        if (fn[0].isalpha() or fn[0]=="√"):
            for ch in fn:
                if ch.isalpha() or ch=='√':
                    st=st+ch
            self.fun(st)
        else:
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
            if fn=="":
                fn="0"
            if sn=="":
                sn=0
        except Exception:
            pass
        if(v=="sin") or(v=="cos") or (v=="tan") or (v=="log") or (v=="√"):
            self.fun(v)

        elif v=="+":
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
                self.error("Can't divide by 0....")
    

    def fun(self, f):
        global v
        n1=self.en.get()
        n=""
        for ch in n1:
            if ch.isnumeric():
                n=n+ch          
        self.en.delete(0, END)
        if n!='':
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
                if(n>0):
                    n=math.sqrt(n)
                    self.en.insert(0, f"{self.val_int(n)}")
                else:
                    self.error("Invalid input")
                
        else:
            self.en.insert(0, f"{f}()")
            v=f


if __name__=="__main__":
    win=Calc()

    entry=win.create_entry(60, 5, "sunken", 0, 0, "Helvetica")

    row,col=0,0
    for i in reversed(range(1, 10)):
        if(i<=3):
            row=3
        elif(i<=6):
            row=2
        else:
            row=1
        button=win.create_button(i, partial(win.show, i), "raised", "bold", row, col)
        if((i-1)%3==0):
            col=0
        else:
            col+=1
            
    b0=win.create_button("0", partial(win.show, 0), "raised", "bold", 4, 0)
    bd0=win.create_button("±", win.change_sign, "raised", "bold", 4, 1)
    bdec=win.create_button(".", partial(win.show, "."), "raised", "bold", 4, 2)

    bdel=win.create_button("DEL", win.back, "raised", "bold", 1, 3)
    bac=win.create_button("AC", win.ac, "raised", "bold", 1, 4)

    bmul=win.create_button("x", partial(win.takef, "x"), "raised", "bold", 2, 3)
    bdiv=win.create_button("/", partial(win.takef, "/"), "raised", "bold", 2, 4)

    bplus=win.create_button("+", partial(win.takef, "+"), "raised", "bold", 3, 3)
    bmin=win.create_button("-", partial(win.takef, "-"), "raised", "bold", 3, 4)

    bper=win.create_button("%", win.per, "raised", "bold", 4, 3)
    beq=win.create_button("=", win.eq, "raised", "bold", 4, 4)

    bsin=win.create_button("sin", partial(win.fun, "sin"), "raised", "bold", 5, 0)
    bcos=win.create_button("cos", partial(win.fun, "cos"), "raised", "bold", 5, 1)
    btan=win.create_button("tan", partial(win.fun, "tan"), "raised", "bold", 5, 2)
    blog=win.create_button("log", partial(win.fun, "log"), "raised", "bold", 5, 3)
    broot=win.create_button("√", partial(win.fun, "√"), "raised", "bold", 5, 4)
        
    win.mainloop()