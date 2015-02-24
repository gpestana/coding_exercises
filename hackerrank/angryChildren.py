#ex1. out: 1335
k = 5
candies = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245,
9948, 2822, 1784, 7802, 3142, 9739, 5629, 5413, 7232]
candies.sort()

#ex2 (0)
k_2 = 2
candies_2 = [1,2,1,2,1]


def solution(k, candies):
  minDiff = None
  res = 0

  currMin_idx = 0  
  currMax_idx = k-1

  for i in xrange(len(candies)-k):
    currMin = candies[currMax_idx] - candies[currMin_idx]
    if not minDiff or minDiff > currMin:
      minDiff = currMin
      res = candies[currMax_idx] - candies[currMin_idx]  

    currMin_idx += 1
    currMax_idx += 1  

  if res < 0:
    return 0
  else:
    return res
  
print solution(k_2, candies_2)
