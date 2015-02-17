class MergeSort:
  
  #O(n) extra space for arrays [O(nlogn) if linked lists]
  #O(nlogn) time

  def sort(self, arr):

    if len(arr) <= 1:
      return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    self.sort(left)
    self.sort(right)
    return list(self.merge(left, right))


  def merge(self, left, right):
    result = []
    left_idx, right_idx = 0, 0
 
    while left_idx < len(left) and right_idx < len(right):
      if left[left_idx] <= right[right_idx]:
        result.append(left[left_idx])
        left_idx += 1      
      else:
        result.append(right[right_idx])
        right_idx += 1

    if left:
      result.extend(left[left_idx:])
    if right:
      result.extend(right[right_idx:])
    
    return result       
