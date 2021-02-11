# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram(s="rat", t="car"))
