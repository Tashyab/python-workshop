# import re
# import math
# def two():
#     a=6
#     b=8
#     return a, b

# # for e in two():
# #     print(e)

# # li=(4, 6, 5, 3)
# # print(two()[0])
# print(math.log(100))
t = int(input())
l=[]
for tc in range(t):
    nl=input()
    a=int(nl.split(" ")[0])
    b=int(nl.split(" ")[1])
    print(a+b)
