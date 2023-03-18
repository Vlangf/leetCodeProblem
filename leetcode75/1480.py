# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    pre = nums[0]
    for i in range(1, len(nums)):
        pre += nums[i]
        nums[i] = pre

    return nums

print(runningSum([3,1,2,10,1]))



