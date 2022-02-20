import itertools

t=int(input())
l=[]
def powfinder(num):
    count=0
    while(num>1):
        num=num/2
        count+=1
    return count

while(t>0):
    n=int(input())
    tot=0
    costl=list(map(int, input().split(" ")))
    powl=tuple(map(powfinder, costl))
    for i in range(1, n+1):
        sublist=tuple(itertools.combinations(powl, i))
        for lists in sublist:
            if sum(lists)%2==0:
                tot+=1
                tot=tot%1000000007
    l.append(tot)
    t-=1

for e in l:
    print(e)

# https://assessment.hackerearth.com/challenges/college/codathon22/algorithm/4a0a65f6e3cd44b0b0cc042771ef0ec6/
