import re
import random
from functools import reduce
import pandas as pd
import numpy as np
import time

# 1
tia = time.time()
# a
arr = np.random.rand(10, 10)
for i, ar in enumerate(arr):
    for ind, e in enumerate(ar):
        arr[i, ind] = e + 10
print(arr)
ta = time.time() - tia

print("\n"*5)

tib = time.time()
# b
arr = np.random.rand(10, 10)
vector = np.full((1, 10), 10)
for i, ar in enumerate(arr):
    arr[i] = ar + vector
print(arr)
tb = time.time() - tib

# c
print(f"Time taken for addition by loop is {ta} and time taken for vector addition is {tb}")

# 2
df = pd.DataFrame(columns=["Roll", "Name",  "Subject", "Age", "Marks"])
# a
for i in range(10):
    student = input(f"Enter roll, name, subject, age, marks for student {i+1}:\n").split(" ")
    student[4] = int(student[4])
    df.loc[i] = student
# b
mean = df.Marks.mean()
max = df.Marks.max()
min = df.Marks.min()
std = df.Marks.std()
print(mean, max, min, std)

# 3
def addit(ls, *args):
    try:
        return sum(ls)
    except Exception as e:
        return (ls + sum(args))


print(addit(12, 23, 43))
print(addit([12, 23, 43]))

# 4
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Anagram") if (reduce(lambda x, y: x+y, sorted(str1)) == reduce(lambda x, y: x+y, sorted(str2))) else print("Non-Angaram")

# 5
# i)
ls = []
for _ in range(9):
    ls.append(random.randint(5, 9))

# ii)
freq = {}
for item in ls:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)

# iii)
mval = max([val for val in freq.values()])
maxklist = []
for key, value in freq.items():
    if(mval == value):
        maxklist.append(key)

for ind, item in enumerate(ls):
    if item in maxklist:
        print(f"Item-{item} Index- {ind}")

# 6
# i) & ii)
ls1 = []
ls2 = []
for _ in range(10):
    ls1.append(random.randint(40, 49))
    ls2.append(random.randint(41, 48))

# iii)
ls3 = []
for i in range(20):
    ls3.append(ls1[i//2]) if(i % 2 == 0) else ls3.append(ls2[i//2])
print(ls1, ls2, ls3)

# 7
def uniquelist(ls):
    uls = []
    freq = {}
    for item in ls:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        if(value == 1):
            uls.append(key)
    print(uls)


uniquelist([1, 2, 1, 4, 32, 32, 34, 4])

# 8
array = np.empty((20, 5), dtype='int16')
arr_new = array[0:10, :]
print(arr_new)

# 9
txt = "-100#^sdfkj8902w3ir021@swf-20"
sumeven = sum(map(int, re.findall(r"\d+", txt)))
sumodd = sum(map(int, re.findall(r"-\d+", txt)))
print(sumeven, sumodd)

# 10
ar = np.array([5, 16, 62, 23, 7, 12, 18, 3, 1])
ind = int(input("Enter the index to split and move: "))
arf = ar[:ind]
ars = ar[ind:]
ar_new = np.concatenate((ars, arf))
print(ar_new)

# 11
a = np.array([[11, 12, 5], [15, 6, 10], [10, 8, 12], [12, 15, 8]])
a_tr = a.transpose()
a_flat = a.ravel()
print("Transposed array: ", a_tr)
print("Flattened array:", a_flat)

# 12
dic = {'a': 100, 'b': 200, 'c': 300}
s = sum([i for i in dic.values()])
print(s)