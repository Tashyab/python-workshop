# l1=[1,2,3]
# l2=[4,5]
# l1=l1+l2
# print(list(reversed(l1)))

n=int(input())
nline=input()
nlist=list(map(int, nline.split(" ")))
nq=int(input())
qline=input()
qlist=list(map(int, qline.split(" ")))

s=sum(nlist)
for q in qlist:
    s=s*2
    print(s)