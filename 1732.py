# 1732. Find the Highest Altitude
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude
# between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
from typing import List
from metrics import benc_time


@benc_time
def largest_altitude(gain: List[int]) -> int:
    highest = 0
    current = 0
    for each in gain:
        current += each
        highest = max(current, highest)

    return highest


@benc_time
def largest_altitude_two(gain: List[int]) -> int:
    highs = [0]
    for each in gain:
        highs.append(each + highs[-1])

    return max(highs)


print(largest_altitude(
    [-4, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3,
     -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4,
     3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3, -2, -1, 4, 3, 2, -3,
     -2, -1, 4, 3, 2]))
