from tkinter import *
from tkinter import messagebox
import requests as req
import json

def news():
    global key
    global fetch_text
    fetch_text=Label(ffetch, text="Fetching news....", font="40")
    fetch_text.pack()
    f3.update()
    q=optvar.get()
    try:
        if "top" in q:
            r=req.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr=json.loads(r.text)
            return start(pr)
        elif "sports" in q:
            r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr = json.loads(r.text)
            return start(pr)
        elif 'entertainment' in q:
            r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr = json.loads(r.text)
            return start(pr)
        elif 'business' in q:
            r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr = json.loads(r.text)
            return start(pr)
    except Exception as e:
        print(e)
        val=messagebox.askretrycancel(title="Retry", message="Check your internet connection!")
        fetch_text.destroy()
        if val:
            news()

def start(pr):
    global nf
    nf=None
    i = 0
    l=[]
    while (i < len(pr['articles'])):
        for key in [*pr['articles'][i]]:
            if key == 'title':
                l.append(pr['articles'][i]['title'])
        i += 1
    f=Frame(f3, border=2, relief=SOLID)
    f.pack(before=nf, pady=5, padx=80)
    nf=f
    fetch_text.destroy()
    for i in l:
        text=Label(nf, text=i, pady=5)
        text.pack()

def dnews():
    try:
        for frames in f3.winfo_children():
            frames.destroy()
    except Exception:
        pass

def close(e):
    val=messagebox.askokcancel(title="Quit", message="Do you want to quit?")
    if val:
        quit()

def closeto():
    val=messagebox.askokcancel(title="Quit", message="Do you want to quit?")
    if val:
        quit()

def save():
    messagebox.showerror(title="Save what!", message="We don't save news, we just show it.")

def saveall():
    messagebox.showinfo(title="Save", message="Use Save button, this does nothing.")

def helping():
    messagebox.showwarning(title="Help", message="We don't provide any help!")

def feedback():
    messagebox.showwarning(title="Feedback", message="We don't believe in feedbacks.")

if __name__=="__main__":
    root=Tk()
    root.title("Newspaper")
    ws=root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    root.geometry(f"{960}x{720}+{int((ws-720)/2)-80}+{20}")
    root.minsize(960, 720)
    root.iconbitmap(r"C:\Users\Acer\3D Objects\Projects\python-workshop\Tkinter/newsp.ico")

    menubar=Menu(root)

    m1=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=m1)
    m1.add_command(label="New", command=dnews)
    m1.add_separator()
    m1.add_command(label="Save",command=save)
    m1.add_command(label="Save All", command=saveall)
    m1.add_separator()
    m1.add_command(label="Quit", command=closeto)

    m2=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=m2)
    m2.add_command(label="Help", command=helping)
    m2.add_separator()
    m2.add_command(label="Send feedback", command=feedback)

    root.config(menu=menubar)

    f1=Frame(root)
    f1.pack()
    optvar=StringVar()
    Label(f1, text="Which headlines would you like to hear? \nTop Headlines, Sports, Entertainment, or Business").pack()
    Radiobutton(f1, text="Top", variable=optvar, value="top").pack(side=LEFT, anchor="n", padx=20)
    Radiobutton(f1, text="Sports", variable=optvar, value="sports").pack(side=LEFT, anchor="n", padx=20)
    Radiobutton(f1, text="Entertainment", variable=optvar, value="entertainment").pack(side=LEFT, anchor="n")
    Radiobutton(f1, text="Business", variable=optvar, value="business").pack()
    optvar.set("top")
    
    f2=Frame(root)
    f2.pack()
    sb=Button(f2, text="SUBMIT", command=news, relief=RAISED, borderwidth=3)
    sb.pack(side=LEFT, anchor="n", padx=5, pady=5)
    db=Button(f2, text="DELETE", command=dnews, relief=RAISED, borderwidth=3)
    db.pack(padx=5, pady=5)

    mf=Frame(root, relief=SOLID)
    mf.pack(fill=BOTH, expand=1)

    can=Canvas(mf)

    scrolly=Scrollbar(mf, orient=VERTICAL, command=can.yview)
    scrolly.pack(fill=Y, side=RIGHT) 

    scrollx=Scrollbar(mf, orient=HORIZONTAL, command=can.xview)
    scrollx.pack(fill=X, side=BOTTOM)

    can.pack(side=LEFT, fill=BOTH, expand=1)

    can.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    can.bind_all("<MouseWheel>", lambda e: can.yview_scroll(int(-1*(e.delta/120)), "units"))
    can.bind_all("<Shift-MouseWheel>", lambda e: can.xview_scroll(int(-1*(e.delta/120)), "units"))
    can.bind('<Configure>', lambda e: can.configure(scrollregion=can.bbox("all")))

    wf=Frame(can)
    can.create_window((0,0), window=wf, anchor="nw")
    
    ffetch=Frame(wf)
    ffetch.pack()
    f3=Frame(wf)
    f3.pack()
    
    for i in range(20):
        Label(wf, text=f" ").pack(pady=10)
    for i in range(100):
        Label(wf, text=f" ").pack(pady=10, side=LEFT)

    root.protocol("WM_DELETE_WINDOW", closeto)
    root.bind_all('<Escape>', lambda e:close(e))

    root.mainloop()
