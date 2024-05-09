import numpy as np
import time

#1

from collections import deque


def bfs(a, b, target):
	m = {}
	isSolvable = False
	path = []

	q = deque()

	q.append((0, 0))

	while (len(q) > 0):
		u = q.popleft()
		if ((u[0], u[1]) in m):
			continue
		if ((u[0] > a or u[1] > b or
                        u[0] < 0 or u[1] < 0)):
			continue
		
		path.append([u[0], u[1]])

		m[(u[0], u[1])] = 1

		if (u[0] == target or u[1] == target):
			isSolvable = True

			if (u[0] == target):
				if (u[1] != 0):
					path.append([u[0], 0])
			else:
				if (u[0] != 0):
					path.append([0, u[1]])
					
			sz = len(path)
			for i in range(sz): 
				print(f"({path[i][0]}, {path[i][1]})")

		q.append([u[0], b])
		q.append([a, u[1]]) 

		for ap in range(max(a, b) + 1):
			c = u[0] + ap
			d = u[1] - ap
			
			if (c == a or (d == 0 and d >= 0)):
				q.append([c, d])

			c = u[0] - ap
			d = u[1] + ap
			
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])

		q.append([a, 0])
		q.append([0, b])

	if (not isSolvable):
		print("No solution")


if __name__ == '__main__':
	m, n, d = 3, 5, 6
	print("Path from initial state to solution state: ")
	bfs(m, n, d)

#2
mean = 0
sd = 1

m1 = int(input("Enter value of m1: "))
n1 = int(input("Enter value of n1: "))
r1 = int(input("Enter value of r1: "))
t1 = np.random.standard_normal(size=(m1, n1, r1))

m2 = int(input("Enter value of m2: "))
n2 = int(input("Enter value of n2: "))
r2 = int(input("Enter value of r2: "))
t2 = np.random.standard_normal(size=(m2, n2, r2))

initial_time = time.time()
c1 = int(input("Enter value for c1: "))
c2 = int(input("Enter value for c2: "))
c3 = int(input("Enter value for c3: "))

t3 = c1*t1+c2*t2+c3

final_time = time.time()
print(t3)
print(f"\nTime for calc.: {final_time - initial_time} ms")
