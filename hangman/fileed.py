import re
list=[]
with open(r"C:\Users\Acer\3D Objects\Projects\python-workshop\hangman\words10raw.txt") as f:
    cont=f.read()
    cont=cont.replace("'","")
    cont=cont.replace( "\n" , " ")
    patt=re.compile(r"[0-9]")
    recont=patt.sub("", cont)
    pat2=re.compile(r"\w{10} | \w\s*\w\s*\w\s*\w\s*\w\s*\w\s*\w\s*\w\s*\w\s*\w")
    wordl=pat2.findall(recont)
    
with open(r"C:\Users\Acer\3D Objects\Projects\python-workshop\hangman\words10.txt", "w") as f:
    f.write("")
with open(r"C:\Users\Acer\3D Objects\Projects\python-workshop\hangman\words10.txt", "a") as f:
    for word in wordl:
        f.write(word+"\n")

        