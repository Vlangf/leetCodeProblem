"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = high + low // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


print(search([12], 12))
