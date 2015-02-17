class Solution:
  # @param num, a list of integer
  # @return an integer
  def findPeakElement(self, num):
    
    biggestIndex = 0

    if len(num) == 1:
      return 0
    if len(num) == 2:
      if num[0]>num[1]:
        return 0
      else:
        return 1
        
    for i in range(1, len(num)):
      if num[i] > num[biggestIndex]:
        biggestIndex = i

      if i+1 !=len(num):
        if num[i-1] < num[i] and num[i] > num[i+1]:
            return i
  
    return biggestIndex

attempt = Solution()
print attempt.findPeakElement([1])
