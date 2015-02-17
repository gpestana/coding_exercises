class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
  def __str__(self):
    return str(self.value)

class MinStack:
  def __init__(self, node=None):
    self.top = node

  def push(self, newNode):
    #if stack is empty
    if not self.top:
      self.top = newNode
      return
    #if newNode is minimum
    if newNode.value < self.top.value:
      newNode.next = self.top
      self.top = newNode
      return
    #placing newNode in the right spot
    prevNode = self.top
    n = self.top
    while(n):
      if newNode.value < n.value:
          prevNode.next = newNode
          newNode.next = n
          return
      prevNode = n
      n = n.next
    #if newNode has the biggest value, place it at the end
    prevNode.next = newNode

  def pop(self):
    popNode = self.top
    self.top = popNode.next
    return popNode

  def show(self):
    n = self.top
    while(n):
      print n
      n = n.next
