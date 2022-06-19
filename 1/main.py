# https://leetcode.com/problems/two-sum/submissions/

def twoSum(nums, target):
  numNeeded = {} # numNeeded, index of known pair

  for i, num in enumerate(nums):
    if (num in numNeeded):
      return [numNeeded[num], i]
    else:
      numNeeded[target - num] = i

# print(twoSum([7,1,3,5,2,11,15], 9))
# print(twoSum([0,4,3,0], 0))
# print(twoSum([-3,4,3,90],0))
