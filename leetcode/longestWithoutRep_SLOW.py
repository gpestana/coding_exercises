class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1

        tmpIdx = 0
        currString = ''
        longest = 0

        for i, c in enumerate(s):
            tmpIdx = i
            while(True):
                if tmpIdx>=len(s):
                  break

                if s[tmpIdx] in currString:
                    if longest < len(currString):
                        longest = len(currString)
                    currString = ''
                    break
                else:
                    currString+=s[tmpIdx]
                    tmpIdx+=1
 
        return longest
                    

at = Solution()
print at.lengthOfLongestSubstring('aa')
        

        
