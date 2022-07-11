# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
  smallestNegativeNumber = None
  largestSum = None
  currentSum = None

  for num in nums:
    
    numIsPositive = num >= 0
    
    if (not numIsPositive and (smallestNegativeNumber == None or num > smallestNegativeNumber)):
      smallestNegativeNumber = num
    
    if currentSum == None:
      if numIsPositive:
        currentSum = num

    else:
      if num * -1 < currentSum:
        currentSum += num
      else:
        currentSum = None

    if currentSum != None and (largestSum == None or currentSum > largestSum):
      largestSum = currentSum

  if largestSum == None:
    return smallestNegativeNumber
  else:
    return largestSum
      
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArray([1])) # 1
print(maxSubArray([5,4,-1,7,8])) # 23