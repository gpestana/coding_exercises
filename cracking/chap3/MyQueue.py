from Stack import *

class MyQueue:
  def __init__(self):
    self.buffer = Stack()
    self.ordered = Stack()

  def enqueue(self, node):
    self.buffer.push(node)

  def dequeue(self):
    queuedNode = self.buffer.pop()
    while queuedNode:
      self.ordered.push(queuedNode)
      queuedNode = self.buffer.pop()
 
    popNode = self.ordered.pop()
 
    orderedNode = self.ordered.pop()
    while orderedNode:
      self.buffer.push(orderedNode)
      orderedNode = self.ordered.pop()
 
    return popNode
