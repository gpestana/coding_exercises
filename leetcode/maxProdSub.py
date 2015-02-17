class Solution:
  
  def maxProduct(self, A):
    currMaxProd = 1
    return r_maxProduct(A, currMaxProd)

def r_maxProduct(A, currMaxProd):
  if not A:
    return currMaxProd 

  prod = 1
  for el in A:  
    prod*=el
   
  if prod > currMaxProd:
    currMaxProd = prod

  return r_maxProduct(A[1:],currMaxProd)
   
 
attempt = Solution()
print attempt.maxProduct([1,0,-1,2,3,-5,-2])
      
