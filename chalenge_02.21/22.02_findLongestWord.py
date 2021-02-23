# Longest Word in Dictionary through Deleting
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting
# some characters of the given string. If there are more than one possible results, return the longest word with
# the smallest lexicographical order. If there is no possible result, return the empty string.
from typing import List
from collections import Counter
from metrics import benc_time


@benc_time
def findLongestWord(s: str, d: List[str]) -> str:
    res = ''
    d.sort(key=len, reverse=True)
    for each in d:
        if len(each) < len(res):
            break
        it = iter(s)
        if all(True if c in it else False for c in each):
            if len(res) < len(each):
                res = each
            else:
                res = min(res, each)

    return res


print(findLongestWord("aewfafwafjlwajflwajflwafj",
                      ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]))
