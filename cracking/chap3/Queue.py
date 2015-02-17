class Node:
  def __init__(self, data):
    self.data = data
    self.next = None  

  def __str__(self):
    return str(self.data)


class Queue:
  def __init__(self, node=None):
    self.front = node
    self.back = node

  def enqueue(self, node):
    if self.front:
      self.back.next = node
      self.back = node
    else:
      self.front = node
      self.back = node

  def dequeue(self):
    if self.front:
      dequeueNode = self.front
      newFront = dequeueNode.next
      self.front = newFront
      return dequeueNode
    else:
      return 'queue is empty' 
    
    
