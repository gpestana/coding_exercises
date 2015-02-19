def partition(arr):
  pivot = 0
  elements = arr[:pivot]+arr[pivot+1:]
  left = [el for el in elements if el < arr[pivot]]
  right = [el for el in elements if el >= arr[pivot]]
  return [left, right, arr[pivot]]

def quickSort(arr):
  if len(arr)>1:
    res = partition(arr)
    left = res[0]
    right = res[1]  
    pivot = res[2]
    return quickSort(left) + [pivot] + quickSort(right)   
  return arr

#print quickSort([5,2,1,7,6])
#print quickSort([1,4,3])
#print quickSort([1,4,66,3,2,56,7,8,9,23])
print quickSort([5,8,1,3,7,9,2])
