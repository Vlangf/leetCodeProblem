# 477. Total Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
from typing import List


def totalHammingDistance(nums: List[int]) -> int:
    result = 0
    while nums:
        last = nums.pop()
        for each in nums:
            result += bin(last | each).count('1')


    return result


print(totalHammingDistance([4, 14, 4]))
