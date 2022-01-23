from cmath import tan
import math
import re
import tkinter as tk
from tkinter.constants import END, RIDGE, SUNKEN, X
from functools import partial

def show(d):
    n=en.get()
    if d=="00" and n!="":
        en.delete(0, END)
        en.insert(0, f"{n}{d}")
    elif d=="0" and n!="0":
        en.delete(0, END)
        en.insert(0, f"{n}{d}")
    elif d=="." and (d not in n):
        en.delete(0, END)
        if n=="":
            en.insert(0, f"{0}{n}{d}")
        else:
            en.insert(0, f"{n}{d}")
    elif (d!=".") and (d!="0") and (d!="00"):
        en.delete(0, END)
        en.insert(0, f"{n}{d}")

def back():
    en.delete(len(en.get())-1, END)
def ac():
    en.delete(0, END)

def getfn():
    global fn
    fn=en.get()
    en.delete(0, END)

def takef(op):
    global v
    v=op
    getfn()

def show_val(k):
    k=float(k)
    if k==int(k):
        k=int(k)
    en.insert(0, f"{k}")

def per():
    nu=float(en.get())
    nu=nu/100
    en.delete(0, END)
    show_val(nu)

def eq():
    global fn
    sn=en.get()
    if v=="+":
        en.delete(0, END)
        sum=(float)(fn)+(float)(sn)
        show_val(sum)

    elif(v=="-"):
        en.delete(0, END)
        diff=(float)(fn)-(float)(sn)
        show_val(diff)

    elif(v=="x"):
        en.delete(0, END)
        pro=(float)(fn)*(float)(sn)
        show_val(pro)

    elif(v=="/"):
        en.delete(0, END)
        di=(float)(fn)/(float)(sn)
        show_val(di)   
    elif(v=="sin") or(v=="cos") or (v=="tan") or (v=="log") or (v=="√"):
        fun(v)
    

def fun(f):
    global v
    n1=en.get()
    n=""
    for ch in n1:
        if ch.isalpha() or ch=='√':
            ch=""
        n=n+ch
    en.delete(0, END)
    if n!='':
        if f=="tan":
            n=float(n)
            n=math.tan(math.radians(n))
            show_val(n)
            
        elif f=="sin":
            n=float(n)
            n=math.sin(math.radians(n))
            show_val(n)

        elif f=="cos":
            n=float(n)
            n=math.cos(math.radians(n))
            show_val(n)

        elif f=="log":
            n=float(n)
            n=math.log10(n)
            show_val(n)

        elif f=="√":
            n=float(n)
            n=math.sqrt(n)
            show_val(n)
    else:
        en.insert(0, f"{f}")
        v=f
        

if __name__=="__main__":
    root=tk.Tk()

    root.title("Calculator")
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    root.geometry(f"516x238+{(int)(sw/2)-200}+200")
    root.maxsize(516, 238)
    root.minsize(516, 238)

    en=tk.Entry(root, width=60, borderwidth=5, relief=SUNKEN)
    en.grid(row=0, column=0, columnspan=5, padx=10, pady=0)
    
    b1=tk.Button(text="1", relief="raised", command=partial(show, 1), font="bold")
    b2=tk.Button(text="2", relief="raised", command=partial(show, 2), font="bold")
    b3=tk.Button(text="3", relief="raised", command=partial(show, 3), font="bold")
    b4=tk.Button(text="4", relief="raised", command=partial(show, 4), font="bold")
    b5=tk.Button(text="5", relief="raised", command=partial(show, 5), font="bold")
    b6=tk.Button(text="6", relief="raised", command=partial(show, 6), font="bold")
    b7=tk.Button(text="7", relief="raised", command=partial(show, 7), font="bold")
    b8=tk.Button(text="8", relief="raised", command=partial(show, 8), font="bold")
    b9=tk.Button(text="9", relief="raised", command=partial(show, 9), font="bold")
    b0=tk.Button(text="0", relief="raised", command=partial(show, "0"), font="bold")
    bd0=tk.Button(text="00", relief="raised", command=partial(show, "00"), font="bold")
    bdec=tk.Button(text=".", relief="raised", command=partial(show, "."), font="bold")

    beq=tk.Button(text="=", relief="raised", command=partial(eq), font="bold")

    bplus=tk.Button(text="+", relief="raised", command=partial(takef, "+"), font="bold")
    bmul=tk.Button(text="x", relief="raised", command=partial(takef, "x"), font="bold")
    bmin=tk.Button(text="-", relief="raised", command=partial(takef, "-"), font="bold")
    bdiv=tk.Button(text="/", relief="raised", command=partial(takef, "/"), font="bold")
    
    bdel=tk.Button(text="DEL", relief="raised", command=back, font="bold")
    bac=tk.Button(text="AC", relief="raised", command=ac, font="bold")

    bper=tk.Button(text="%", relief="raised", command=per, font="bold")

    bsin=tk.Button(text="sin", relief="raised", command=partial(fun, "sin"), font="bold")
    bcos=tk.Button(text="cos", relief="raised", command=partial(fun, "cos"), font="bold")
    btan=tk.Button(text="tan", relief="raised", command=partial(fun, "tan"), font="bold")
    blog=tk.Button(text="log", relief="raised", command=partial(fun, "log"), font="bold")
    broot=tk.Button(text="√", relief="raised", command=partial(fun, "√"), font="bold")

    b9.grid(row=1, column=0, sticky=tk.E+tk.W)
    b8.grid(row=1, column=1, sticky=tk.E+tk.W)
    b7.grid(row=1, column=2, sticky=tk.E+tk.W)
    b6.grid(row=2, column=0, sticky=tk.E+tk.W)
    b5.grid(row=2, column=1, sticky=tk.E+tk.W)
    b4.grid(row=2, column=2, sticky=tk.E+tk.W)
    b3.grid(row=3, column=0, sticky=tk.E+tk.W)
    b2.grid(row=3, column=1, sticky=tk.E+tk.W)
    b1.grid(row=3, column=2, sticky=tk.E+tk.W)
    b0.grid(row=4, column=0, sticky=tk.E+tk.W)
    bd0.grid(row=4, column=1, sticky=tk.E+tk.W)
    bdec.grid(row=4, column=2, sticky=tk.E+tk.W)

    bplus.grid(row=3, column=3, sticky=tk.E+tk.W)
    bmin.grid(row=3, column=4, sticky=tk.E+tk.W)
    bmul.grid(row=2, column=3, sticky=tk.E+tk.W)
    bdiv.grid(row=2, column=4, sticky=tk.E+tk.W)

    bdel.grid(row=1, column=3, sticky=tk.E+tk.W)
    bac.grid(row=1, column=4, sticky=tk.E+tk.W)
    bper.grid(row=4, column=3, sticky=tk.E+tk.W)
    beq.grid(row=4, column=4, sticky=tk.E+tk.W)

    bsin.grid(row=5, column=0, sticky=tk.E+tk.W)
    bcos.grid(row=5, column=1, sticky=tk.E+tk.W)
    btan.grid(row=5, column=2, sticky=tk.E+tk.W)
    blog.grid(row=5, column=3, sticky=tk.E+tk.W)
    broot.grid(row=5, column=4, sticky=tk.E+tk.W)

    root.mainloop()
