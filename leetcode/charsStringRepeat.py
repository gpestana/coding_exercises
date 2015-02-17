#longest substring without repeating chars
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
      longestSubstring = 0

      if len(s) == 0:
        return 0
      if len(s) == 1:
        return 1

      for index, char in enumerate(s):
        sizeSubstring = self.checkSubstring(index, s)
        if sizeSubstring>longestSubstring:
          longestSubstring = sizeSubstring

      if sizeSubstring > longestSubstring:
        return sizeSubstring
      else:
        return longestSubstring

    def checkSubstring(self, starting, s):
      currSubstring = []
      for index in range(starting, len(s)):
        if s[index] not in currSubstring:
          currSubstring.append(s[index])
        else:
          return len(currSubstring) 
      return len(currSubstring)

attempt = Solution()
print attempt.lengthOfLongestSubstring('pwwkew') #3: pwwkew
print attempt.lengthOfLongestSubstring('p') #1: p
print attempt.lengthOfLongestSubstring('') #0 
print attempt.lengthOfLongestSubstring('au') #2 
print attempt.lengthOfLongestSubstring('dvdf') #3
