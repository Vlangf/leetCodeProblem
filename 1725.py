# 1725. Number Of Rectangles That Can Form The Largest Square
# You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length
# li and width wi.
# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi.
# For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
# Return the number of rectangles that can make a square with a side length of maxLen.
from typing import List
from metrics import benc_time


@benc_time
def count_good_rectangles(rectangles: List[List[int]]) -> int:
    sq_dict = {}
    for each in rectangles:
        side = min(each)
        if side in sq_dict:
            sq_dict[side] += 1
        else:
            sq_dict[side] = 1

    return sq_dict[max(sq_dict.keys())]


@benc_time
def count_good_rectangles_two(rectangles: List[List[int]]) -> int:
    sq_dict = []
    for each in rectangles:
        sq_dict.append(min(each))

    return sq_dict.count(max(sq_dict))


@benc_time
def count_good_rectangles_three(rectangles: List[List[int]]) -> int:
    max_side = 0
    count = 1
    for each in rectangles:
        m = min(each)
        if m > max_side:
            max_side = m
            count = 1
        elif m == max_side:
            count += 1

    return count


from collections import Counter


@benc_time
def count_good_rectangles_four(rectangles: List[List[int]]) -> int:
    sides = Counter(map(min, rectangles))
    return sides[max(sides)]


print(count_good_rectangles_four([[2, 3], [3, 7], [4, 3], [3, 7]]))
