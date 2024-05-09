import random
import sys

l=[]
st=""
n=int(input("Enter the number characters: "))
i=0
print("Entern the characters-")
while(i<n):
    ch= input()
    if len(ch)>1:
        print("Enter a single character only!")
        continue
    l.append(ch)
    i+=1
i=0
a=0
while(i<399):
    if(a==3):
        st=st+ " "
        a=0
        continue
    else:
        k=random.choice(l)
        st=st+f"{k}"
    a+=1
    i+=1
print(f"\n{st}")