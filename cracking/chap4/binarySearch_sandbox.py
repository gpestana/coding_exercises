from BTree import *

arr = [5, 3, 4, 20, 30, 25, 40]
root = BinaryTree(10)

for v in arr:
  branch = BinaryTree(v)
  addBinarySearchTree(root, branch)
  
#depthFirst_preorder(root) 

breathFirst(root)
