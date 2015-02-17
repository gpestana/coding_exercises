class Solution:
  def __init__(self):
    self.longest = 0
    self.lastIndex = 0    

  # @return an integer
  def lengthOfLongestSubstring(self, s):
    while True:
      finalIndex = transverse(self.lastIndex, s)
      if finalIndex == len(s)-1:
        return self.longest
      else:
        self.lastIndex+=1
        finalIndex = transverse(self.lastIndex, s)
 
def transverse(lastIndex, s):
  substring = []
  for i in range(lastIndex, len(s)):
    print s[i]
    if s[i] in substring:
      if len(substring) > self.longest:
        longest = len(substring)
        return i
    else:
      substring.append(s[i])
    return i

attempt = Solution()
print attempt.lengthOfLongestSubstring('dvdf') #3
