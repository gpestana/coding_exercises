import math

def calcLine(n, r):
  if n == r:
    return str(1)
  return str(math.factorial(n)/(math.factorial(r)*math.factorial(n-r))) + ' ' + calcLine(n, r+1)


def calcPascal(n, maxLine):
  if n > maxLine:
    return ''
  return calcLine(n, 0)+'\n'+calcPascal(n+1, maxLine)


if __name__ == '__main__':
  print calcPascal(0, 10)
