# 1742. Maximum Number of Balls in a Box
# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit
# inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number.
# For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in
# the box number 1 + 0 = 1.
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
from metrics import benc_time


@benc_time
def count_balls(low_limit: int, high_limit: int) -> int:
    bol_boxes = {}
    for i in range(low_limit, high_limit + 1):
        s = sum(map(int, str(i)))
        bol_boxes[s] = bol_boxes.get(s, 0) + 1

    return max(bol_boxes.values())


@benc_time
def count_balls_two(low_limit: int, high_limit: int) -> int:
    bol_boxes = [0] * 60
    for i in range(low_limit, high_limit + 1):
        bol_boxes[sum(map(int, str(i)))] += 1

    return max(bol_boxes)


@benc_time
def count_balls_three(low_limit: int, high_limit: int) -> int:
    bol_boxes = {}
    ret = 0
    for i in range(low_limit, high_limit + 1):
        boll = 0
        while i:
            boll += i % 10
            i //= 10
        bol_boxes[boll] = bol_boxes.get(boll, 0) + 1
        ret = max(ret, bol_boxes[boll])
    return ret


print(count_balls_three(1, 1000000))
