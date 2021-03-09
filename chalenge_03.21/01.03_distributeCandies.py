# Distribute Candies
# Alice has n candies, where the ith candy is of type candyType[i].
# Alice noticed that she started to gain weight, so she visited a doctor.
#
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
# Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still
# following the doctor's advice.
#
# Given the integer array candyType of length n, return the maximum number of different types of candies she can
# eat if she only eats n / 2 of them.
from typing import List


def distributeCandies(candyType: List[int]) -> int:
    max_n = len(candyType) // 2
    uniq_t = len(set(candyType))
    return uniq_t if max_n >= uniq_t else max_n


print(distributeCandies([1, 2]))
