import tkinter as tk
from tkinter.constants import ANCHOR, X, Y, BOTH
from PIL import Image, ImageTk

root=tk.Tk()

ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=int((ws-450)/2)
y=int((hs-800)/2)
root.geometry(f"{360}x{640}+{x}+{y}")
root.minsize(640,360)
root.maxsize(ws,hs)

text=tk.Label(text="THIS IS A FUCKING ZOMBIE", bg="grey", fg="maroon", font=("Times new roman", 20, "italic bold"),
    borderwidth=10, relief="ridge", height="2", width="24")
text.pack(side="bottom")

photo=tk.PhotoImage(file="self.png")
# imgm=Image.open("self.jpeg")
# photo=ImageTk.PhotoImage(imgm)
img=tk.Label(image=photo, cursor="spider", borderwidth=10, relief="ridge")
img.pack(side="bottom")

root.mainloop()