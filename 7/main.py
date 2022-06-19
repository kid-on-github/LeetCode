# https://leetcode.com/problems/reverse-integer/

def reverse(x):
  numList = list(str(x))

  isNegative = numList[0] == '-'

  start = 0
  if(isNegative):
    start = 1


  numLen = len(numList)
  isOddLength = not (numLen % 2 == 0)
  middle = int(numLen+isOddLength/2)

  for start in range(start, middle):
    end = len(numList) - start
    print(start, end)
    # tmp = numList[start]
    # numList[start] = numList[end]
    # numList[end] = tmp

  return int(''.join(numList))


print(reverse(-1200))
print('\n\n')
print(reverse(120))


# def reverse(x):
#     numList = list(str(x))
#     isNegativeAsInt = numList[0] == '-'
#     reversedNums = []

#     for i in range(len(numList)-isNegativeAsInt):
#         reversedNums.append(numList[len(numList)-1-i])
#     reversedInt = int(''.join(reversedNums))

#     if isNegativeAsInt:
#         return reversedInt * -1
#     return reversedInt


# print(reverse(-1200))
# print('\n\n')
# print(reverse(120))
