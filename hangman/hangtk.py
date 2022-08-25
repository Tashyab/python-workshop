from tkinter import *

if __name__=="__main__":
    root=Tk()
    root.title("Hangman")
    ws=root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    root.geometry(f"{960}x{720}+{int((ws-720)/2)-80}+{20}")
    root.minsize(960, 720)

    


    root.mainloop()
