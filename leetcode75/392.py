# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions of
# the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s, t):
    l_s = len(s)
    i = 0
    for each in t:
        if i == l_s:
            return True
        elif each == s[i]:
            i += 1

    return i == l_s


print(isSubsequence(s="j", t=""))
