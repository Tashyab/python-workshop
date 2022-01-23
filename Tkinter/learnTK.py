from cProfile import label
from msilib.schema import RadioButton
from re import S
import tkinter as tk
from tkinter import HORIZONTAL, RIGHT, Button, Canvas, Frame, IntVar, Listbox, PhotoImage, Scale, Scrollbar, messagebox, Label
from tkinter.constants import ANCHOR, LEFT, SOLID, SUNKEN, X, Y, BOTH, TOP
from tkinter.ttk import Label
from typing import Text
from PIL import Image, ImageTk
import time

from pygame import QUIT

root=tk.Tk()

root.title("GUI Tutorials")
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=int((ws-450)/2)
y=int((hs-800)/2)
root.geometry(f"{720}x{640}+{x}+{y}")


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

# def funtos(eveent):
#     a=tk.Label(text="I am qutting moterfucker")
#     a.pack(side=TOP)

# def fun(event):
#     a=tk.Label(text=f"You clicked ({event.x},{event.y})")
#     a.pack(side=TOP)

# def funny(event):
#     a=tk.Label(text=f"You clicked {event.char}")
#     a.pack(side=TOP)

# widget=tk.Button(root, text="press me bitch")
# widget.pack()
# widget.bind("<Button-1>", funtos)
# widget.bind("<Button-3>", fun)
# widget.bind("<Key>", funny)
# widget.bind("<Alt-e>", quit)

# def customsize():
#     root.geometry(f"{enterw.get()}x{enterh.get()}")
# tk.Label(text="Enter width").pack()
# enterw=tk.Entry(root)
# enterw.pack()
# tk.Label(text="Enter height").pack()
# enterh=tk.Entry(root)
# enterh.pack()
# cbut=tk.Button(root, text="CUSTOMIZE", command=customsize).pack()
# cbut=tk.Button(root, text="QUIT", command=quit).pack()

# def myfunc():
#     tk.Label(text="Hola Day").pack()

# mend=tk.Menu(root)
# mend.add_command(label="menu", command=myfunc)
# mend.add_command(label="Exit", command=exit)
# root.config(menu=mend) 

# def exitreq():
#     value=messagebox.askyesno(title="Exit", message="Are you sure?")
#     print(value)
#     if value==True:
#         quit()

# def helpme():
#     v1=messagebox.showerror(title="Help", message="We don't help people.")
#     print(type(v1))


# def feedback():
#     v2=messagebox.showwarning(title="Feedback", message="Sorry, We don't believe in feedbacks.")
#     print(v2)

# def saving():
#     v3=messagebox.showinfo(title="Save", message="We don't save file, complete your work amd fuck off!")
#     print(type(v3))


# menubar=tk.Menu(root)
# m1=tk.Menu(menubar, tearoff=0, relief=SOLID, activeforeground="green", activebackground="white", activeborderwidth=4)
# m1.add_command(label="New File",command=myfunc)
# m1.add_command(label="Open File", command=myfunc)
# m1.add_separator()
# m1.add_command(label="Save File", command=saving)
# m1.add_separator()
# m1.add_command(label="Exit", command=exitreq)
# menubar.add_cascade(label="File", menu=m1)

# m2=tk.Menu(menubar, tearoff=0)
# m2.add_command(label="Help", command=helpme)
# m2.add_separator()
# m2.add_command(label="Send Feedback", command=feedback)
# menubar.add_cascade(label="Help", menu=m2)
# root.config(menu=menubar)

# def ratethis():
#     rating=slider.get()
#     radiorating=ratevar.get()
#     if (rating <=3 and rating >0) or (radiorating<=3 and radiorating>0):
#         messagebox.showerror(title="Fuck You", message="Rate us 5 stars you asshole.")
#     if rating ==4 or radiorating==4:
#         messagebox.showwarning(title="Hey You", message="Rate us 5 stars, we don't accept 4s.")
#     if rating==5 or radiorating==5:
#         messagebox.showinfo(title="Thanks", message="Thank You.")

# slider=Scale(root, label="Rate it bitch....", from_=0, to=5, orient=HORIZONTAL, length=200, sliderlength=45,
# tickinterval=1, troughcolor="black")
# slider.pack()

# ratevar=IntVar()
# # ratevar.set(5)
# ige=PhotoImage(file="self.png")

# radio=tk.Radiobutton(root, text="1 star", variable=ratevar, value=1).pack()
# radio=tk.Radiobutton(root, text="2 star", variable=ratevar, value=2).pack()
# radio=tk.Radiobutton(root, text="3 star", variable=ratevar, value=3).pack()
# radio=tk.Radiobutton(root, text="4 star", variable=ratevar, value=4).pack()
# radio=tk.Radiobutton(root, text="5 star", variable=ratevar, value=5).pack()

# Button(text="Submit", pady=5, command=ratethis).pack(pady=5)
# f1=Frame(root)
# f1.pack()
# scb=Scrollbar(f1)
# scb.pack(side="right", fill=Y)

# lbx=Listbox(f1, yscrollcommand=scb.set)
# for i in range(300):
#     lbx.insert(tk.END, f'{i+1}')
# lbx.pack()
# scb.config(command=lbx.yview)
def close(e):
    val=messagebox.askokcancel(title="Quit", message="Do you want to quit?")
    if val:
        quit()

root.bind_all('<Escape>', lambda e:close(e))
mf=Frame(root, border=2, relief=SOLID)
mf.pack(fill=BOTH, expand=1)

can=Canvas(mf)
can.pack(side=LEFT, fill=BOTH, expand=1)

scrolly=Scrollbar(mf, orient=tk.VERTICAL, command=can.yview)
scrolly.pack(fill=Y, side=RIGHT) 

can.config(yscrollcommand=scrolly.set)
can.bind_all("<MouseWheel>", lambda e: can.yview_scroll(int(-1*(e.delta/120)), "units"))
can.bind('<Configure>', lambda e: can.configure(scrollregion=can.bbox("all")))

wf=Frame(can)
can.create_window((0,0), window=wf, anchor="nw")

for i in range(100):
    Button(wf, text=f"button {i+1}").pack(pady=10)

root.mainloop()