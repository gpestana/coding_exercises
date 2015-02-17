from LinkedLists import LinkedList
from LinkedLists import Node

def removeDup(list):
  existNodes = {}
  node = list.head
  while(node != None):
    if node.data not in existNodes:
      existNodes[node.data] = node.data
    else:
      prevNode.next = node.next
      prevNode = prevNode
      node = node.next
      continue
    prevNode = node
    node = node.next


def lastNth(l, n):
  nth = n
  runnerNode = l.head
  nthNode = l.head
  
  while n != 1:
    runnerNode = runnerNode.next
    n-=1

  while runnerNode.next != None:
    runnerNode = runnerNode.next
    nthNode = nthNode.next

  print str(nth)+'nth from the end: '+str(nthNode)

node1 = Node(5)
node2 = Node(1)
node3 = Node(3)

node4 = Node(2)
node5 = Node(9)
node6 = Node(5)

l1 = LinkedList()
l1.insert(node1)
l1.insert(node2)
l1.insert(node3)

l2 = LinkedList()
l2.insert(node4)
l2.insert(node5)
l2.insert(node6)

l1.show()
print '--'
l2.show()

 
