from MinStack import *

stack = MinStack()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n32 = Node(32)
n12 = Node(12)
n6 = Node(6)

stack.push(n1)
stack.push(n2)
stack.push(n32)
stack.push(n2)
stack.push(n6)

print stack.pop()
print stack.pop()
print '--'
stack.show()
