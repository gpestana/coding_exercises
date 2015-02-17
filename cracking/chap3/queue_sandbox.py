from Queue import *

queue = Queue()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

queue.enqueue(node1)
queue.enqueue(node3)
queue.enqueue(node2)
queue.enqueue(node4)

print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
