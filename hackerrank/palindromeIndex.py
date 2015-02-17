#!/usr/bin/python
import fileinput 

def detectIntruder(str):
  arr = list(str)
  i, j = 0, len(arr)-1
  
  while i <= j:
    if arr[i] != arr[j]:
      if arr[i] == arr[j-1]:
        return j
      else:
        return i
    i+=1
    j-=1  
  return -1


if __name__ == '__main__':
  nrInput = int(raw_input())
  for i in xrange(nrInput):
    s = raw_input()
    print detectIntruder(s) 

#print detectIntruder('aaab')      #3
#print detectIntruder('baa')       #0
#print detectIntruder('aaa')       #-1
#print detectIntruder('ABCDDCFBA') #6
