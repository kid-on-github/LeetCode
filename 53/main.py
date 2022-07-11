# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
  largestSum = nums[0]
  currentSum = None

  for num in nums:
    
    if currentSum != None:
      currentSum += num
      if currentSum < 1:
        currentSum = None

    else:
      if num >= 0:
        currentSum = num
      elif num > largestSum:
        largestSum = num

    if currentSum != None and currentSum > largestSum:
      largestSum = currentSum

  return largestSum
      
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArray([1])) # 1
print(maxSubArray([5,4,-1,7,8])) # 23
print(maxSubArray([-2,1])) # 1
print(maxSubArray([-1,0])) # 0

