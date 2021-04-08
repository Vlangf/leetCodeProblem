# Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
# could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
# any letters.

from typing import List


def letterCombinations(digits: str) -> List[str]:
    map_d_l = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    if digits == '':
        return []
    first = map_d_l[digits[0]]
    for i in range(1, len(digits)):
        res = []
        for each in first:
            res += list(map(lambda x: each + x, map_d_l[digits[i]]))
            first = res

    return first


print(letterCombinations(""))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
