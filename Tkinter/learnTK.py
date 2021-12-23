import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()

ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=int((ws-450)/2)
y=int((hs-800)/2)
root.geometry(f"{360}x{640}+{x}+{y}")
root.minsize(640,360)
root.maxsize(ws,hs)

text=tk.Label(text="THIS IS A FUCKING ZOMBIE")
text.pack()

photo=tk.PhotoImage(file="self.png")
# imgm=Image.open("self.jpeg")
# photo=ImageTk.PhotoImage(imgm)
img=tk.Label(image=photo)
img.pack()

root.mainloop()