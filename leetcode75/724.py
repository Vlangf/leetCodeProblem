# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to
# the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no
# elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start_sum = 0
    end_sum = sum(nums)
    for i in range(len(nums)):
        end_sum -= nums[i]
        if end_sum == start_sum:
            return i
        start_sum += nums[i]

    return -1

print(pivotIndex(nums = [1,7,3,6,5,6]))