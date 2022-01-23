
n=int(input())
nline=input()
nlist=list(map(int, nline.split(" ")))
clist=[]
for i in nlist:
    clist.append(i)

nq=int(input())
qline=input()
qlist=list(map(int, qline.split(" ")))

for q in qlist:
    i=0
    if q>=0:
        while(i<len(nlist)):
            if(i>=q):
                nlist[i]=clist[i-q]
            else:
                nlist[i]=clist[len(nlist)-q+i]
            i+=1
    else:
        q=abs(q)
        while(i<len(nlist)):
            if(i<len(nlist)-q):
                nlist[i]=clist[i+q]
            else:
                nlist[i]=clist[i-len(nlist)+q]
            i+=1

    nlist=clist+nlist
    clist=[]
    for i in nlist:
        clist.append(i)
    print(sum(nlist))



