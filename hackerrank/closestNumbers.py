#!/usr/bin/python

def process(arr):
  currPairs = []
  currClosest = ''
  arr.sort()

  idx_A = 0
  idx_B = 1

  for i in xrange(len(arr)-1):
    calc = abs(arr[idx_A] - arr[idx_B])
    if not currClosest:
      currClosest = calc
    if calc < currClosest:
      currClosest = calc
      currPairs = []
    if calc == currClosest:
      currPairs.append(arr[idx_A])
      currPairs.append(arr[idx_B])   
    idx_A+=1
    idx_B+=1

  return currPairs

if __name__ == '__main__':
  inputArray = []
  nrInput = int(raw_input())
  for i in xrage(nrInput):
    n = int(raw_input())
    inputArray.append(n)

  res = process(inputArray)
  for p in res:
    print p


#print process([-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854])
#print process([-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854,-520,-470])
#print process([-20,3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854])


