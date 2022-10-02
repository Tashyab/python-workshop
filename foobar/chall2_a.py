sol_list=[]

class Node:
    def __init__(self, d=None):
        self.data = d
        self.left = None
        self.right = None


def createTree(h, l):
    if h == 1:
        return Node(l.pop())
    node = Node()
    node.data = l.pop()
    node.right = createTree(h-1, l)
    node.left = createTree(h-1, l)
    return node

def findVal(root, v, p):
    if root == None:
        return
    if root.data == v:
        sol_list.append(p)
    else:
        findVal(root.left, v, root.data)
        findVal(root.right, v, root.data)

def printpost(root):
    if root is not None:
        printpost(root.left)
        printpost(root.right)
        print(root.data)
    

def solution(h, q):
    l = list(range(1, 2**h))
    root = createTree(h, l)
    for qs in q:
        findVal(root, qs, -1)
    return ",".join(list(map(str, sol_list)))
    

print(solution(3, [7, 3, 5, 1]))


