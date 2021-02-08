# 914. X of a Kind in a Deck of Cards
# In a deck of cards, each card has an integer written on it.
# Return true if and only if you can choose X >= 2 such that it is possible to split
# the entire deck into 1 or more groups of cards, where:
#   Each group has exactly X cards.
#   All the cards in each group have the same integer.
from functools import reduce
from typing import List
from collections import Counter
from metrics import benc_time


@benc_time
def has_groups_sizeX(deck: List[int]) -> bool:
    if len(deck) < 2:
        return False
    cards = Counter(deck)
    x = min(cards.values())
    if x < 2:
        return False
    while x != 2 and x % 2 == 0:
        x //= 2
    for i in range(2, x + 1):
        flag = True
        for k, v in cards.items():
            if v % i != 0:
                flag = False
        if flag:
            return True

    return False


from math import gcd


@benc_time
def hasGroupsSizeX(deck):
    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2


print(hasGroupsSizeX([1]))
