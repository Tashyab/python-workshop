from tkinter.constants import DISABLED, END, NORMAL, RAISED, SOLID
import requests as req
import json
import tkinter as tk

def news():
    global key
    global intext
    key=0
    q=qval.get()
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
    else:
        intext=tk.Label(root, text=f"Not a valid choice. Retry.")
        intext.pack()
        key=1
        sb['state']=DISABLED
        ent.delete(0, END)

def start(pr):
    global nf
    i = 0
    l=[]
    while (i < len(pr['articles'])):
        for key in [*pr['articles'][i]]:
            if key == 'title':
                l.append(pr['articles'][i]['title'])
        i += 1
    nf=tk.Frame(root, borderwidth=2, relief=SOLID)
    nf.pack()
    for i in l:
        text=tk.Label(nf, text=i)
        text.pack()
    ent.delete(0, END)
    sb['state']=DISABLED



def dnews():
    if key==0:
        nf.destroy()
    else: intext.destroy()
    sb['state']=NORMAL

if __name__=="__main__":
    root=tk.Tk()
    root.title("Newspaper")
    ws=root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    root.geometry(f"{960}x{680}+{int((ws-720)/2)-80}+{20}")
    root.minsize(720, 480)
    tk.Label(text="Which headlines would you like to hear? Top Headlines, Sports, Entertainment, or Business"
    "\nEnter top, sports, entertainment, or business:").pack()
    qval=tk.StringVar()
    ent=tk.Entry(root, textvariable=qval, borderwidth=2)
    ent.pack()
    sb=tk.Button(text="SUBMIT", command=news, relief=RAISED, borderwidth=3)
    sb.pack(pady=5)
    db=tk.Button(text="DELETE", command=dnews, relief=RAISED, borderwidth=3)
    db.pack(pady=5)

    root.mainloop()
