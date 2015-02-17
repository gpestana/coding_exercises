from BTree import *

root = BinaryTree('F')

branch1 = BinaryTree('B')
branch2 = BinaryTree('A')
branch3 = BinaryTree('D')
branch4 = BinaryTree('C')
branch5 = BinaryTree('E')
branch6 = BinaryTree('G')
branch7 = BinaryTree('I')
branch8 = BinaryTree('H')

root.setLeftChild(branch1)
root.setRightChild(branch6)
branch1.setLeftChild(branch2)
branch1.setRightChild(branch3)
branch3.setLeftChild(branch4)
branch3.setRightChild(branch5)
branch6.setRightChild(branch7)
branch7.setLeftChild(branch8)

print 'pre-order:'
depthFirst_preorder(root)

print 'in-order:'
depthFirst_inorder(root)

print 'post-order'
depthFirst_postorder(root)
