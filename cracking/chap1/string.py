#implement algorithm that determines if string has repeated chars

class Chapter1:
  
  def checkUniqueChar(self, string):
    existChars = {}
    for char in string:
      if char in existChars:
        return True
      else:
        existChars[char] = None    
    return False

  def checkUniqueCharNoStructure(self, string):
    lastChar = ''
    for char in sorted(string):
      if lastChar == char:
        return True
      lastChar = char
    return False 

  def areAnagrams(self, str1, str2):
    charsInStrs = {}
    if len(str1) != len(str2):
      return False
   
    for i in range(0, len(str1)):
      if str1[i] not in charsInStrs:
        charsInStrs[str1[i]] = 1
      else:
        charsInStrs[str1[i]] += 1

      if str2[i] not in charsInStrs:
        charsInStrs[str2[i]] = -1
      else:
        charsInStrs[str2[i]] -= 1

      print charsInStrs

    for k, val in charsInStrs.iteritems():
      if val != 0:
        return False
      
    return True

  def areAnagrams2(self, str1, str2):
    if sorted(str1) == sorted(str2):
      return True
    else:
      return False
        

  
          
chp1 = Chapter1()

print chp1.areAnagrams2('ewqqwe','qweqwe')
