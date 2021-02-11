# Shortest Distance to a Character
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
# and answer[i] is the shortest distance from s[i] to the character c in s.
from typing import List


def shortestToChar(s: str, c: str) -> List[int]:
    c_arr = []
    res = []
    for i, x in enumerate(s):
        res.append(i)
        if x == c:
            c_arr.append(i)

    c_arr.append(10 ** 4 + 1)
    last = -(10 ** 4 + 1)
    i = 0
    for each in c_arr:
        while i <= each and i < len(s):
            res[i] = min(res[i] - last, each - res[i])
            i += 1
        last = each

    return res


def shortestToChar_two(S, C):
    last = float('-inf')
    res = []
    for i, x in enumerate(S):
        if x == C:
            last = i
        res.append(i - last)

    last = float('inf')
    for i in range(len(S) - 1, -1, -1):
        if S[i] == C:
            last = i
        res[i] = min(res[i], last - i)
    return res


print(shortestToChar_two("loveleetcode", "e"))
