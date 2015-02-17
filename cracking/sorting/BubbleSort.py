class BubbleSort:

#Stable
#O(1) extra space (does not require any special data structure)
#O(n^2) in the comparisons and swaps
  
  def sort(self, arr):
    swapped = False
    for i in xrange(len(arr)-1):
      if arr[i]>arr[i+1]:
        swap(arr, i)
        swapped = True
    if swapped == True:
      self.sort(arr)
    
    return arr

def swap(arr, i):
  buff = arr[i]
  arr[i] = arr[i+1]
  arr[i+1] = buff
