 


    

import random

class TreeNode:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                tempNode = TreeNode()
                self.left = tempNode
                self.left.data = data
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                tempNode = TreeNode()
                self.right = tempNode
                self.right.data = data
            else:
                self.right.insert(data)
    
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverseInOrder()

def createRoot():
    i = random.randint(0, 10)
    rootNode = TreeNode()
    rootNode.data = i
    return rootNode

def createTree():
    rootNode = createRoot()
    numNodes = random.randint(1, 10)
    j = 0
    L = []
    while j <= numNodes:
        newVal = random.randint(1, 20)
        if newVal not in L:
            rootNode.insert(newVal)
            L.append(newVal)
            j += 1
    return rootNode

def getSum(node):
    if node is None:
        return 0
    else:
        leftSum = getSum(node.left)
        rightSum = getSum(node.right)
        return node.data + leftSum + rightSum

rootNode = createTree()
print("Inorder Traversal:")
rootNode.traverseInOrder()
print("\nSum =", getSum(rootNode))

