#!/usr/bin/py
def lonelyinteger(inputArr):
    auxArr = []
    for el in inputArr:
      if el not in auxArr:
        auxArr.append(el)
      else:
        auxArr.remove(el) 
    return auxArr[0] 


if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
