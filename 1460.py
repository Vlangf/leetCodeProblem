# 1460. Make Two Arrays Equal by Reversing Sub-arrays
# Given two integer arrays of equal length target and arr.
# In one step, you can select any non-empty sub-array of arr and reverse it.
# You are allowed to make any number of steps.
# Return True if you can make arr equal to target, or False otherwise.
from typing import List
from metrics import benc_time
from collections import Counter


@benc_time
def can_be_equal(target: List[int], arr: List[int]) -> bool:
    if Counter(target) == Counter(arr):
        return True

    return False


@benc_time
def can_be_equal_two(target: List[int], arr: List[int]) -> bool:
    for each in target:
        if not target.count(each) == arr.count(each):
            return False

    return True


@benc_time
def can_be_equal_three(target: List[int], arr: List[int]) -> bool:
    dict_nums = dict(zip(target, arr))
    return sum(dict_nums.keys()) - sum(dict_nums.keys()) == 0


print(can_be_equal_two(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
