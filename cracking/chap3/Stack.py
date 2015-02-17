class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)


class Stack:
  def __init__(self, top=None):
    self.top = top

  def pop(self):
    if self.top != None:
      obj = self.top
      self.top = obj.next 
      return obj
    else:
      return None
  
  def push(self, obj):
    if self.top == None:
      self.top = obj
    else:
      prevTop = self.top
      obj.next = prevTop
      self.top = obj
