import math

def isPalindrome(x):
  x = str(x)
  for i in range(math.floor(len(x)/2)):
    if x[i] != x[-1 * (i+1)]:
      return False
  
  return True


x = [
  121,
  1221,
  1234,
  11133111
]
for i in x:
  print(isPalindrome(i))

