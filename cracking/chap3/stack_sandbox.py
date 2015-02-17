from Stack import *

stack = Stack()
obj1  = Node(1)
obj2  = Node(2)
obj5  = Node(5)

stack.push(obj1)
stack.push(obj2)


print "popped: "+str(stack.pop())
print "popped: "+str(stack.pop())
print "popped: "+str(stack.pop())
print "popped: "+str(stack.pop())
stack.push(obj5)
print "popped: "+str(stack.pop())
print "popped: "+str(stack.pop())
