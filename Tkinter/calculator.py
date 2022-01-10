import tkinter as tk
from tkinter.constants import RIDGE, X


if __name__=="__main__":
    root=tk.Tk()

    root.title("TAshCalc")
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    root.geometry(f"420x560+{(int)(sw/2)-200}+40")
    root.maxsize(420, 560)
    root.minsize(420, 560)

    en=tk.Entry(root, width=52, borderwidth=2, relief=RIDGE).grid(pady=4, columnspan=5)
    
    b1=tk.Button(text="1", relief="raised", pady=4, padx=16)
    b2=tk.Button(text="2", relief="raised", pady=4, padx=16)
    b3=tk.Button(text="3", relief="raised", pady=4, padx=16)
    b4=tk.Button(text="4", relief="raised", pady=4, padx=16)
    b5=tk.Button(text="5", relief="raised", pady=4, padx=16)
    b6=tk.Button(text="6", relief="raised", pady=4, padx=16)
    b7=tk.Button(text="7", relief="raised", pady=4, padx=16)
    b8=tk.Button(text="8", relief="raised", pady=4, padx=16)
    b9=tk.Button(text="9", relief="raised", pady=4, padx=16)
    b0=tk.Button(text="0", relief="raised", pady=4, padx=16)

    b9.grid(row=1, column=0)
    b8.grid(row=1, column=1)
    b7.grid(row=1, column=2)
    b6.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b4.grid(row=2, column=2)
    b3.grid(row=3, column=0)
    b2.grid(row=3, column=1)
    b1.grid(row=3, column=2)
    b0.grid(row=4, column=1)

    root.mainloop()
