m=input("Enter the value of Divisor(M) in binary: ")
q=input("Enter the value of dividend(Q) in binary: ")
a="".join(["0" for i in range(len(q)+1)])
m="".join(["0" for i in range(len(q)-len(m)+1)])+m

def sumbin(a, b):
    sum= bin(int(a, 2) + int(b, 2))[2:]
    if(len(sum)==len(a)):
        return sum
    else:
        return sum[1:]

def twos(nl):
    for iter, i in enumerate(nl):
        if i==0:
            nl[iter]=1
        else:
            nl[iter]=0
    nl=sumbin("".join(list(map(str, nl))), "1")
    return nl

negm="".join(list((twos([int (i) for i in m]))))

def ls(a, b):
    a=[int(i) for i in a]
    b=[int(i) for i in b]
    for iter, i in enumerate(a):
        if(iter<len(a)-1):
            a[iter]=a[iter+1]
        else:
            a[iter]=b[0]
    a="".join(list(map(str, a)))

    for iter, i in enumerate(b):
        if(iter<len(b)-1):
            b[iter]=b[iter+1]
        else:
            b[iter]="_"
    b="".join(list(map(str, b)))
    
    return [a, b]
    

for nt in range(len(q)):
    if(a[0]=='0'):
        print(f"{ls(a, q)[0]}\t{ls(a,q)[1]}")

        a=sumbin(ls(a, q)[0],negm)
        q=ls(a, q)[1]

        print(f"{a}\t{q}")
        if(a[0]=='0'):
            q=q[:len(q)-1]+"1"
        else:
            q=q[:len(q)-1]+"0"
        print(f"{a}\t{q}")
    else:
        print(f"{ls(a, q)[0]}\t{ls(a,q)[1]}")

        a=sumbin(ls(a, q)[0],m)
        q=ls(a, q)[1]

        print(f"{a}\t{q}")
        if(a[0]=='0'):
            q=q[:len(q)-1]+"1"
        else:
            q=q[:len(q)-1]+"0"
        print(f"{a}\t{q}")
    print("\n")