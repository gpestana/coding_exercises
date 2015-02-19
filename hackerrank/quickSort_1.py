#!/bin/python

def partition(ar, low, high):    
    biggerP = []
    smallerP = []
    p = ar[0]
  
    for i in xrange(low, high):
        if ar[i]>p:
            biggerP.append(ar[i])
        elif ar[i]<p:
            smallerP.append(ar[i])  

    return [smallerP, biggerP]
    #return smallerP+[p]+biggerP


def quicksort(arr, low, high):
  if len(arr) < 1:
    return

  res = partition(arr, low, high)
  quicksort(arr, low, high-1)
  quicksort(arr, low+1, high)


#m = input()
#ar = [int(i) for i in raw_input().strip().split()]
#print ' '.join([str(nr) for nr in partition(ar)])


arr = [5,2,1,7,6]
print quicksort(arr, 0, len(arr))
