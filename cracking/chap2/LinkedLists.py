class Node:
  def __init__(self, data):
    self.next = None
    self.data = data
  
  def __str__(self):
    return str(self.data)


class LinkedList:
  def __init__(self):
    self.head = None
 
  def insert(self, node):
    if not self.head:
      self.head = node
    else:
      n = self.head
      while(n.next != None):
        n = n.next
      n.next = node

  def delete(self, data):
    #edge case when head is to be deleted
    if self.head.data == data:
      self.head = self.head.next
      return
    node = self.head
    while(node.data != data):
      prevNode = node
      node = node.next
    
    if(node.data == data):
      prevNode.next = node.next 
    else:
      print 'cannot delete: node doesnt exist' 

  def show(self):
    node = self.head
    while(node != None):
      print node
      node = node.next
