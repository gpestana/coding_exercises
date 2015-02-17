class Node:
  def __init__(self, value):
    self.value = value
  
  def __str__(self):
    return str(value)

class ArrayStack:
  def __init__(self):
    self.MAX_SIZE = 3
    self.STACK_1 = 0
    self.STACK_2 = 3
    self.STACK_3 = 6
    self.array = [None]*9

  def push(stack, node):
    top = self.getTopStack(stack)
    if 3%top !=0:
      self.array[top] = node  
    else:
      return 'stack '+str(stack)+' is full' 

  def pull(self, stack):
    top = self.getTopStack(stack)
    self.array[top] = None
    return top   

  def getTopStack(self, stack):
    if stack == 1:
      s = self.STACK_1
    elif stack == 2:
      s = self.STACK_2
    else:
      s = self.STACK_3

    for n in reversed(range(s, s+3)):
      if not n:
        return n
    return s
