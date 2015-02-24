def fib(n, fibHash):
  if n == 0:
    return 0
  if n == 1:
    return 1

  
  res = fib(n-1, fibHash) + fib(n-2, fibHash)
  if res in fibHash:
    fibHash[res] = 'isFibo'

  return res

if __name__ == '__main__':
  times = input()
  fibHash = {}
  maxInput = 0
  order = []

  for i in xrange(times):
    inp = input()
    fibHash[inp] = 'IsNotFibo'
    maxInput = inp if inp > maxInput else None
    order.append(inp) 

  fib(maxInput, fibHash)
  for res in order:
    print fibHash[res] 
