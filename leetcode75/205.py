# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving
# the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    comp_dict = {}
    for i, each in enumerate(s):
        if not comp_dict.get(each):
            if t[i] not in comp_dict.values():
                comp_dict[each] = t[i]
            else:
                return False
        elif comp_dict[each] != t[i]:
            return False

    return True


print(isIsomorphic(s="bbbaaaba", t="aaabbbba"))
