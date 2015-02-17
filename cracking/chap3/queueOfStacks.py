from MyQueue import *

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

queue = MyQueue()

queue.enqueue(n1)
queue.enqueue(n3)
queue.enqueue(n2)
queue.enqueue(n4)

print queue.dequeue()
print queue.dequeue()
queue.enqueue(n1)
print queue.dequeue()
