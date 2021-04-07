# Determine if String Halves Are Alike
# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
# Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
from metrics import benc_time


@benc_time
def halvesAreAlike(s: str) -> bool:
    h_l = len(s) // 2
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    c_1, c_2 = 0, 0
    for i in range(h_l):
        if s[i] in vowels:
            c_1 += 1

        if s[i + h_l] in vowels:
            c_2 += 1

    return c_1 == c_2


@benc_time
def halvesAreAlike_two(s: str) -> bool:
    h_l = len(s) // 2
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    c_1, c_2 = sum((1 for x in s[:h_l] if x in vowels)), sum((1 for x in s[h_l:] if x in vowels))

    return c_1 == c_2


print(halvesAreAlike_two("book"))
