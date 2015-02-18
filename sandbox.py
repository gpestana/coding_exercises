def recursiveSum(arr):
  if len(arr) == 1:
    return arr[0]
  
  return arr[0] + recursiveSum(arr[1:])

print recursiveSum([1,3,5,4])
