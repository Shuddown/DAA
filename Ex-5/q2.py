 
import random as rn
import matplotlib.pyplot as plt
import numpy as np

def random_points(n: int, min_x: int, min_y: int, max_x: int, max_y: int) -> list[tuple[int,int]]:
    
    def random_tuple(min_x: int, min_y: int, max_x: int, max_y: int) -> tuple[int,int]:
        return (rn.randint(min_x, max_x), rn.randint(min_y, max_y))
    
    return [random_tuple(min_x, min_y, max_x, max_y) for _ in range(n)]

def dist(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    x_diff =  (point1[0] - point2[0])
    y_diff = (point1[1] - point2[1])
    return (x_diff * x_diff + y_diff * y_diff) ** (1/2)

def sort_points(points: list[tuple[int,int]]) -> list[tuple[int,int]]:
    return sorted(points, key = lambda x: (x[0], x[1]))

def closest_pair(sorted_points: list[tuple[int,int]]) -> list[tuple[int,int]]:
    if len(sorted_points) <= 2:
        return sorted_points
    
    mid = len(sorted_points) // 2 
    # plt.axvline(x=sorted_points[mid][0], color = 'red', linestyle = '-', linewidth = 2)
    min_pair_left = closest_pair(sorted_points[mid:])
    min_pair_right = closest_pair(sorted_points[:mid])
    left_min_dist = float('inf') if len(min_pair_left) < 2 else dist(min_pair_left[0], min_pair_left[1])  
    right_min_dist = float('inf') if len(min_pair_right) < 2 else dist(min_pair_right[0], min_pair_right[1])  
    min_dist = min(left_min_dist, right_min_dist)
    min_pair = min_pair_left if min_dist == left_min_dist else min_pair_right
    x_min = sorted_points[mid][0] - min_dist
    x_max = sorted_points[mid][0] + min_dist
    left_points = []
    right_points = []
    
    for point in sorted_points[mid:]:
        if(point[0] > x_max): break
        left_points.append(point)
    
    for point in sorted_points[mid - 1::-1]:
        if(point[0] < x_min): break
        right_points.append(point)
    
    
    for left_point in left_points:
        for right_point in right_points:
            if(dist(left_point, right_point) < min_dist):
                min_dist = dist(left_point, right_point)
                min_pair = (left_point, right_point)
    
    return min_pair
            
    
        
 
points = random_points(10000, 0, 0, 1000000, 10000000)
points = sort_points(points)
x = np.array([point[0] for point in points])
y = np.array([point[1] for point in points])
scatter = plt.scatter(x,y,color = 'blue')
min_pair = closest_pair(points)
plt.plot(min_pair[0][0], min_pair[0][1], 'ro')
plt.plot(min_pair[1][0], min_pair[1][1], 'ro')
# for i in range(len(points)):
#     plt.text(x[i], y[i], str((x[i], y[i])))
plt.show()


    

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

