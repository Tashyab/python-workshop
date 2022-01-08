import tkinter as tk
from tkinter.constants import ANCHOR, LEFT, SOLID, SUNKEN, X, Y, BOTH, TOP
from typing import Text
from PIL import Image, ImageTk
import time

root=tk.Tk()

root.title("GUI Tutorials")
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=int((ws-450)/2)
y=int((hs-800)/2)
root.geometry(f"{720}x{640}+{x}+{y}")
root.minsize(320,180)
root.maxsize(ws,hs)

# text=tk.Label(text="THIS IS A FUCKING ZOMBIE", bg="grey", fg="maroon", font=("Times new roman", 20, "italic bold"),
#     borderwidth=10, relief="ridge", height="2", width="24")
# text.pack(side="bottom")

# photo=tk.PhotoImage(file="self.png")
# # imgm=Image.open("self.jpeg")
# # photo=ImageTk.PhotoImage(imgm)
# img=tk.Label(image=photo, cursor="spider", borderwidth=10, relief="ridge")
# img.pack(side="bottom")


# f1=tk.Frame(root, bg="blue")
# f1.pack(side=LEFT, fill=Y)
# l1=tk.Label(f1, text="Project tkinter", bg="blue", fg="white", font="bold", padx=6, pady=4)
# l1.pack(side=LEFT, anchor="n")

# f2=tk.Frame(root, bg="red")
# f2.pack(side=TOP, fill=X)
# l2=tk.Label(f2, text="Python Workshop", bg="red", fg="white", font="bold", padx=6, pady=4)
# l2.pack(side=TOP, anchor="w")

# def useless():
#     text=tk.Label(text="Don't click me asshole", bg="grey", fg="maroon", font=("Times new roman", 20, "italic bold"),
#     borderwidth=10, relief=SOLID, height="2", width="24")
#     text.pack(side="bottom", anchor="w")

# f3=tk.Frame(root, padx=10, pady=10)
# f3.pack(side=LEFT, anchor="nw")
# b1=tk.Button(f3, fg="white", bg="black", text="USELESS BUTTON",  relief=SUNKEN, command=useless)
# b1.pack()


# def getvals():
#     if(cbv.get()==1):
#         un=f"{uv.get()} is username"
#         ps=f"{pv.get()} is password"
#         tk.Label(root, text=un).grid()
#         tk.Label(root, text=ps).grid()
# uv=tk.StringVar()
# pv=tk.StringVar()
# cbv=tk.IntVar()
# user=tk.Label(root, text="username")
# pasw=tk.Label(root, text="password")
# user.grid()
# pasw.grid(row=1)
# uentry=tk.Entry(root, textvariable=uv)
# pentry=tk.Entry(root, textvariable=pv)
# uentry.grid(row=0, column=1)
# pentry.grid(row=1, column=1)
# tk.Checkbutton(text="Check it to submit", variable=cbv).grid()
# tk.Button(text="SUBMIT", command=getvals, padx=2, pady=2).grid()


# cw=tk.Canvas(root, width=ws, height=hs, border=4, relief=SOLID)
# cw.pack()
# cw.create_rectangle(20, 20, ws-20, hs-100, activefill="green", width=2, outline="green")
# cw.create_oval(20, 20, ws-20, hs-100, activefill="yellow", width=2, outline="yellow")
# cw.create_line(20, 20, ws-20, hs-100, fill="red", width=2)
# cw.create_line(ws-20, 20, 20, hs-100, fill="blue", width=2)
# cw.create_line(ws/2, 20, ws/2, hs-100, fill="blue", width=2)
# cw.create_line(20, hs/2-40, ws-20, hs/2-40, fill="red", width=2)
# cw.create_polygon([20, 20, 20, 100, 100, 100, 100, 20], width=3)

def funtos(eveent):
    a=tk.Label(text="I am qutting moterfucker")
    a.pack(side=TOP)

def fun(event):
    a=tk.Label(text=f"You clicked ({event.x},{event.y})")
    a.pack(side=TOP)

def funny(event):
    a=tk.Label(text=f"You clicked {event.char}")
    a.pack(side=TOP)

widget=tk.Button(root, text="press me bitch")
widget.pack()
widget.bind("<Button-1>", funtos)
widget.bind("<Button-3>", fun)
widget.bind("<Key>", funny)
widget.bind("<Alt-e>", quit)

root.mainloop()