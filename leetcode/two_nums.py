# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    #first iteration
    firstSum = sum(l1.val, l2.val)
    lnode = ListNode(firstSum[0])
    carry = firstSum[1]
    l1 = l1.next
    l2 = l2.next 
    prevNode = lnode

    while l1 != None:
      res = sum(l1, l2)
      newNode = ListNode(res[0]+carry)
      carry = res[1]
      prevNode.next = newNode
      prevnode = newNode 

    return lnode

  def sum(self, n1, n2):
    if n1+n2 > 9:
      return [(n1+n2)%10,1]
    else:
      return [n1+n2, 0]


s = Solution()
#s.addTwoNumbers(l1, l2)

