
t=int(input())
l=[]

while(t>0):
    inp=list(map(int, input().split(" ")))
    n=inp[0]
    k=inp[1]
    m=inp[2]

    wb=input()
    lwb=[]
    for ball in wb:
        lwb.append(int(ball))

    i=0
    while(i<m):
        lwb_temp=[]
        for ball in lwb:
            if(ball==0):
                lwb_temp.append(0)
                continue
            nb=ball*k        
            nb=str(nb)
            for b in nb:
                lwb_temp.append(int(b))
        lwb=lwb_temp
        i+=1
    l.append(len(lwb)%1000000007)
    t-=1

for e in l:
    print(e)

# https://www.codechef.com/FEB221C/problems/DIGMULK