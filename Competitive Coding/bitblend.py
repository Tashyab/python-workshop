
def add_pos_to_list(opos, n, l):
    i=0
    if(opos%2==0):
        i=1
    else:
        i=2
    while(i<=n):
        if(i!=opos+1):
            l.append(f"{i} {opos+1}")
        i+=2

t=int(input())
l=[]

while(t>0):
    n=int(input())
    inp=list(map(int, input().split(" ")))
    on=0
    en=0
    en_ep=0
    en_op=0
    on_ep=0
    on_op=0
    elist=[]
    olist=[]
    for it, num in enumerate(reversed(inp)):
        if num%2==0:
            epos=n-it-1
            en+=1
            elist.append(epos) #stores epos from last to first
            if epos%2==0:
                en_ep+=1
            else:
                en_op+=1
        else:
            opos=n-it-1
            on+=1
            olist.append(opos) #stores opos from last to first
            if opos%2==0:
                on_ep+=1
            else:
                on_op+=1

    if(on==0):
        l.append(-1)
    elif(on==1):
        if(n%2==0):
            m=(n-2)/2
        else:
            if(opos%2==0):
                m=n//2
            else:
                m=(n//2)-1
        l.append(m)
        add_pos_to_list(opos, n, l)

    elif(on>=2):   
        i=0
        m=0
        temp_l=[]
        if ((on>=en) and (on_op>=on_ep)) or ((en>on) and (en_ep>en_op)):
            #make even at ep and odd at op
            while(i<n):
                if(i%2==0) and (inp[i]%2==1):
                    m+=1
                    if(olist[0]!=i):
                        temp_l.append(f"{i+1} {olist[0]+1}")
                    else:
                        temp_l.append(f"{i+1} {olist[1]+1}")
                elif(i%2==1) and (inp[i]%2==0):
                    m+=1
                    temp_l.append(f"{i+1} {olist[0]+1}")
                i+=1                   
        else:
            #make even at op and odd at ep
            while(i<n):
                if(i%2==1) and (inp[i]%2==1):
                    m+=1
                    if(olist[0]!=i):
                        temp_l.append(f"{i+1} {olist[0]+1}")
                    else:
                        temp_l.append(f"{i+1} {olist[1]+1}")
                elif(i%2==0) and (inp[i]%2==0):
                    m+=1
                    temp_l.append(f"{i+1} {olist[0]+1}")
                i+=1
        l.append(m)
        for items in temp_l:
            l.append(items)
    t-=1

for e in l:
    print(e)

# https://www.codechef.com/FEB221C/problems/BITBLEND
