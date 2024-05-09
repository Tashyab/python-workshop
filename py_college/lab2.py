import numpy as np
import time
import math

#1
p = np.random.rand(10^6, 10^4)
q = np.random.rand(10^6, 10^4)

r1 = np.empty((10^6, 10^6))
#a

q_ts = q.transpose()

row, col = 0, 0

ti1 = time.time()
for i in p:
    for j in q:
        r1[row][col] = sum(i*j)
        col += 1
    row += 1
    col = 0
print(r1)
t1 = time.time() - ti1

#b
print("\n\n")
ti2 = time.time()
r2 = p@q_ts
print(r2)
t2 = time.time() - ti2

#c 
print(round((t1/t2), 2))


#2
p = np.random.randint(1, 100, 10)
q = np.random.randint(1, 100, 10)
print(p, q)

#a
eud = np.sqrt(sum(np.square(q-p)))
print(eud)

#b
pm = np.mean(p)
qm = np.mean(q)
pcc = sum((p - pm)*(q - qm))/math.sqrt(sum(np.square(p - pm))*sum(np.square(q - qm)))
print(pcc)


#3
p = np.array([2, 1, 2])
q = np.array([1, 1, 1])

cos = sum(p*q)/(math.sqrt(sum(np.square(p))*sum(np.square(q))))
angle = math.acos(cos)
print(round(angle/math.pi * 180, 2), "degrees")


#4
a = np.random.randint(1, 10, (3,3))
b = np.random.randint(1, 10, (3,3))

x = np.transpose(a) @ b
print(x)
w1 = np.linalg.eigvals(a @ b)
w2 = np.linalg.eigvals(b @ a)
print(w1)
print(w2)


#5
a = np.random.rand(1, 100, 10)
b = np.random.rand(1, 100, 10)

#a
d = sum(abs(a - b))
print("The manahattan distance is ", d)

#b
ar = np.arange(16)
ar = ar.reshape(4, 4)
a = np.matrix(ar)

#6
x = np.random.rand(3, 3)
pdf = np.empty(9)
xm = np.mean(x)
xsd = np.std(x)

i = 0
for xi in x.ravel():
    pdfi = math.exp(-1/2 * ((xi-xm)/xsd))/(2*np.pi*math.pow(xm, 2))
    pdf[i] = pdfi
    i += 1

pdf = pdf.reshape(3,3)
print(pdf)


#7
#a
ar = np.random.randint(1, 100, 10)

#b
arm = np.mean(ar)
arsd = np.sqrt(sum(np.square(ar - arm))/10)
print(arsd, "\n\n")


#8
x = np.random.randint(1, 100, (3,3))
y = np.random.randint(1, 100, (3,3))

#b
xinvy = np.linalg.inv(x) @ y
xtrx = x @ np.transpose(x)
xtry = x @ np.transpose(y)

print(xinvy, xtrx, xtry)


#9
n = 15
arr = np.random.randint(1, 100, n)
arrm = sum(arr)/n
print("Mean: ", arrm)
arr_sorted = np.sort(arr)
print("Median: ", end = "")
print(arr_sorted[n//2 + 1]) if n%2==1 else print(arr_sorted[n//2])
var = sum(np.square(arr - arrm))/n
dev = np.std(arr)
print("Variance: ", var)
print("Deviation: ", dev)


#10
x = np.random.randint(1, 100, (3, 2))

p = int(input("Enter the value of p: "))
minkd = math.pow(sum(np.power(abs(np.diff(x)), p)), 1/p)
print(minkd)


#11
def normalizeRows(x):
    x = x/np.sqrt(np.sum(np.square(x), 1))
    return x

x = np.random.randint(1, 100, (4, 4))
print(normalizeRows(x))


#12
x1 = np.array([9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0])
x2 = np.array([9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0])

print(np.sum(x1*x2))
