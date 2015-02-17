class Solution:
  # @param num, a list of integers
  # @return an integer
  def majorityElement(self, num):
    if len(num) == 0:
      return 0
    if len(num) == 1:
      return num[0]

    nums = {}
    minimum = len(num)/2
    for n in num:
      if n in nums:  
        nums[n]+=1
        if nums[n] == minimum:
          return n
      else:
        nums[n] = 0


att = Solution()
print att.majorityElement([1,2,2,2,3])
