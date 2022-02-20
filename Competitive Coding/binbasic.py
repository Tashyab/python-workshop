
def check_pal(bin):
    binrev=bin[::-1]
    if bin==binrev:
        return True

t=int(input())
l=[]
while(t>0):
    inp=list(map(int, input().split(" ")))
    n=inp[0]
    k=inp[1]
    bin=input()

    key=0
    i=0
    if(k==0):
        if check_pal(bin):
            l.append("Yes")
        else:
            l.append("No")
    else:
        if(k>0):
            if(n%2==0):
                while(i<n/2):
                    if(bin[i]!=bin[n-i-1]):
                        key+=1
                    i+=1
                if ((key%2==0) and (k>=key) and (k%2==0)) or ((key%2==1) and (k>=key) and (k%2==1)):
                    l.append("Yes")
                else:
                    l.append("No")
            else:
                while(i<n//2):
                    if(bin[i]!=bin[n-i-1]):
                        key+=1
                    i+=1
                if(k>=key):
                    l.append("Yes")
                else:
                    l.append("No")          
    t-=1

for e in l:
    print(e)