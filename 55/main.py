# https://leetcode.com/problems/jump-game/submissions/

import json


def canJump(nums):
    indexesThatCanReachEnd = {}

    # loop through the numbers in reverse starting from the second to last number
    nums.pop()
    nums.reverse()

    for i, num in enumerate(nums):
        canJumpToEnd = num > i

        if (canJumpToEnd):
            indexesThatCanReachEnd[i] = None
        else:
            if num == 0:
                continue
            # check to see if there are any valid jumps within reach
            for ii in range(1, num+1):
                if (i-ii in indexesThatCanReachEnd):
                    indexesThatCanReachEnd[i] = None
                    break

    if (len(nums) == 0):
        return True
    if (len(indexesThatCanReachEnd) == 0):
        return False
    return len(nums)-1 in indexesThatCanReachEnd


casesToTest = {
    '[2,3,1,1,4]': True,
    '[3,2,1,0,4]': False,
    '[0]': True,
    '[0,1]': False,
    '[1,2]': True,
    '[0,2,3]': False,
}

for case in casesToTest.keys():
    expected = casesToTest[case]
    returned = canJump(json.loads(case))
    if (expected == returned):
        pass
    else:
        print(case, f'FAIL: expected {expected}, but received {returned}\n\n')
