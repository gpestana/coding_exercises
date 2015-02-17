class Solution:
  def firstMissingPositive(self, arr):
    if not arr:
      return 1

    res = checkArrayComplete(arr)
    if res:
      return res
    else:
      return checkFirstMissing(arr)

def checkArrayComplete(arr):
  maxEl = None
  minEl = None
  positiveLen, continousLen = 0, 0

  for el in arr:
    if el > 0:
      if not maxEl: maxEl = el
      if not minEl: minEl = el
      positiveLen+=1
      if el > maxEl: maxEl = el
      if el < minEl: minEl = el

  if not maxEl: 
    return False

  continousLen = (maxEl - minEl + 1)
  
  if continousLen == positiveLen:
    if minEl > 1:
      return 1
    else:
      return maxEl+1
  else:
    return False 

def checkFirstMissing(arr):
  firstMissing = None
  for el in arr:
    if not firstMissing and el > 0:
      firstMissing = el
  
    if firstMissing and el > 0 and el < firstMissing:
      firstMissing = el

  if not firstMissing:
    firstMissing = 0

  if firstMissing > 1:
    return 1
  else: 
    return firstMissing+1

attempt = Solution()
#print attempt.firstMissingPositive([1,2,0]) #3
#print attempt.firstMissingPositive([3,4,-1,1]) #2
#print attempt.firstMissingPositive([2]) #1
#print attempt.firstMissingPositive([2,1]) #3
#print attempt.firstMissingPositive([1,0]) #2
#print attempt.firstMissingPositive([2,2]) #1
#print attempt.firstMissingPositive([-5,1000]) #1
print attempt.firstMissingPositive([0]) #1
#print attempt.firstMissingPositive([0,1,2]) #3
