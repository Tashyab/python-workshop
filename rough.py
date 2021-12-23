# Content file editor

import os
os.chdir(r"C:\Users\Acer\3D Objects\Projects\python-workshop")
l=os.listdir()
with open(r"C:\Users\Acer\3D Objects\Projects\python-workshop\content.txt", "w") as f:
    f.write("")
with open(r"C:\Users\Acer\3D Objects\Projects\python-workshop\content.txt", "r+") as f:
    for nm in l:
        f.write(f"{nm}\n")



