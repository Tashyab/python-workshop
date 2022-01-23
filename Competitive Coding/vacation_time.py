import math

def pf(n):
    a=0
    pro=1
    l=[]
    while(n%2==0):
        a+=1
        n=n/2
    if(a%2!=0):
        l.append(2)
    i=3
    while(i<int(math.sqrt(n))+1):
        a=0
        while(n%i==0):
            a+=1
            n=n/i
        if(a%2!=0):
            l.append(i)
        i+=2
    if n>2:
        l.append(int(n))

    for item in l:
        pro=pro*item
    return pro

if __name__=="__main__":
    n=int(input("Enter the number: "))
    temp=n
    key=0
    while(True):
        key+=1
        p=n*pf(n)
        if(int(math.sqrt(p))<n):
            n=int(math.sqrt(p))
        else:
            break
    
    print(n, key)

