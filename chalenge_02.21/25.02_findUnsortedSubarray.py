# Shortest Unsorted Continuous Subarray
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray
# in ascending order, then the whole array will be sorted in ascending order.
# Return the shortest such subarray and output its length.
from typing import List


def findUnsortedSubarray(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0

    sor = sorted(nums)
    if sor == nums:
        return 0

    s, e = 0, 0

    for i in range(len(nums)):
        if nums[i] != sor[i]:
            s = i
            break

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != sor[i]:
            e = i
            break

    return e - s + 1


print(findUnsortedSubarray(nums = [2,6,4,8,10,9,15]))
