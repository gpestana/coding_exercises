class BinaryTree:
  def __init__(self, value=None, leftChild=None, rightChild=None):
    self.value = value
    self.left = leftChild
    self.right = rightChild

  def __str__(self):
      if self.value:
        return str(self.value)
      else:
        return 'empty tree'

  def setRightChild(self, child):
     self.right = child

  def setLeftChild(self, child):
     self.left = child

  def getRightChild(self):
    return self.right

  def getLeftChild(self):
    return self.left

  def setValue(self, value):
    self.value = value
  
  def getValue(self):
    return self.value


def depthFirst_preorder(root):
  if not root:
    return
  print root
  depthFirst_preorder(root.getLeftChild())
  depthFirst_preorder(root.getRightChild())

def depthFirst_inorder(root):
  if not root:
    return
  depthFirst_inorder(root.getLeftChild())
  print root
  depthFirst_inorder(root.getRightChild())

def depthFirst_postorder(root):
  if not root:
    return
  depthFirst_postorder(root.getLeftChild())
  depthFirst_postorder(root.getRightChild())
  print root

def breathFirst(root):
  q = []
  def queue(q, el):
    q.append(el)
  def dequeue(q):
    if len(q)>0:
      val = q[0]
      del q[0]
      return val
    else:
      return None
 
  queue(q, root)
  while len(q)>0:
    node = dequeue(q)
    if node:
      print node
    left = node.getLeftChild()
    right = node.getRightChild()
    if left:
      queue(q, left)
    if right:
      queue(q, right)

def addBinarySearchTree(root, node):
  if node.value > root.value:
    right = root.getRightChild()
    if right:
      addBinarySearchTree(root.getRightChild(), node)
    else:
      root.setRightChild(node)
      return

  if node.value <= root.value:
    left = root.getLeftChild()
    if left:
      addBinarySearchTree(root.getLeftChild(), node)
    else:
      root.setLeftChild(node)
      return
