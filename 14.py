# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List
from metrics import benc_time


@benc_time
def longest_common_prefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ''

    prefix = strs[0]
    for each in strs:
        if not each.startswith(prefix):
            prefix = ''.join([x if x == y else ':' for x, y in zip(prefix, each)]).split(':')[0]
            if prefix == '':
                break

    return prefix


print(longest_common_prefix(["dog", "racecar", "car"]))
