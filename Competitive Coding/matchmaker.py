
t=int(input())
l=[]
for test in range(t):
    n=int(input())
    bl=list(map(int, input().split(" ")))
    gl=list(map(int, input().split(" ")))
    m=n//2
    count=0
    key=0
    if(n%2==0):
        for i in range(n//2):
            if (bl[m-i-1]==gl[m-i-1]):
                if(bl[m+i]==gl[m+i]):
                    key=0
                else:
                    count=-1
                    break
            elif(bl[m-i-1]==gl[m+i]):
                if key==0:
                    count+=1
                    key=1
            else:
                count=-1
                break
    else:
        for i in range(n//2 + 1):
            if (bl[m-i]==gl[m-i]):
                if(bl[m+i]==gl[m+i]):
                    key=0
                else:
                    count=-1
                    break
            elif(bl[m-i]==gl[m+i]):
                if key==0:
                    count+=1
                    key=1
            else:
                count=-1
                break

    l.append(count)
        
for e in l:
    print(e)
# https://assessment.hackerearth.com/challenges/college/codathon22/algorithm/288a45fc8d074036b9596433de332cd3/