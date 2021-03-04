# Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
# due to some error, one of the numbers in s got duplicated to another number in the set, which results in r
# epetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        if nums[i] - 1 != nums[i - 1]:
            if nums[i] - 2 == nums[i - 1]:
                return [nums[i], nums[i] - 1]
            else:
                return [nums[i], nums[i] + 1]


print(findErrorNums([2,2]))
