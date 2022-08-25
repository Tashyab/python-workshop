import numpy as np
import sys

# ar1=np.array([2, 3, 4, 43, 22, 11])
# ar2=np.array([24, 23, 54, 6, 32, 1])

# print(ar1+ar2)
# print(ar1-ar2)
# print(ar1*ar2)
# print(ar1/ar2)
# print(ar1%ar2)
# print(np.sqrt(ar1))
# print(np.square(ar2), "\n")

# py_ar=[0, 4, 55, 2, 5, 33]
# pyar=[88, 9, 335, 12, 25, 3]
# np_ar=np.array([py_ar, pyar])

# print(sys.getsizeof(1)*len(py_ar))
# print(np_ar.dtype)
# print(np_ar.itemsize)

ar=np.array([[1,2,3], [4,5,6], [7,1,0]])
# print(ar)
# print(ar.argsort(axis=0))
# print(np.eye(4), "\n")
# print(np.identity(4))


# np.random.seed(129)
# o = np.random.randint(0, 10, size = (5,5))
# np.random.seed(123)
# k = np.random.randint(0, 10, size = (5,5))
# np.random.seed(129)
# b = np.random.randint(0, 10, size = (5,5))
# np.random.seed(123)
# itch = np.random.randint(0, 5, size = (5,5))

# print(f"{o}\n\n{k}\n\n{b}\n\n{itch}")

arr=np.array([1, 2, 3, 4, 5])
a=arr[3:]
print(a)