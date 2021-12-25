import time
import requests as req
import json
import tkinter as tk

def start(pr):
    i = 0
    l=[]
    while (i < len(pr['articles'])):
        for key in [*pr['articles'][i]]:
            if key == 'title':
                l.append(pr['articles'][i]['title'])
        i += 1
    return l

def news():
    print("Which headlines would you like to hear? Top Headlines, Sports, Entertainment, or Business")
    q=input("Enter top, sports, entertainment, or business: ")
    if "top" in q:
        r=req.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
        pr=json.loads(r.text)
        start(pr)
    elif "sports" in q:
        r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
        pr = json.loads(r.text)
        start(pr)
    elif 'entertainment' in q:
        r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
        pr = json.loads(r.text)
        start(pr)
    elif 'business' in q:
        r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
        pr = json.loads(r.text)
        start(pr)
    else:
        print("Not a valid choice.")
    return start(pr)

if __name__=="__main__":
    l=news()
    root=tk.Tk()
    ws=root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    root.geometry(f"{980}x{560}+{int((ws-720)/2)}+{int((hs-480)/2)}")
    root.minsize(720, 480)
    for i in l:
        text=tk.Label(text=i)
        text.pack()
    root.mainloop()
