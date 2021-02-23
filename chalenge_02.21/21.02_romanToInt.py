# Roman to Integer
# Given a roman numeral, convert it to an integer.
from metrics import benc_time


@benc_time
def romanToInt(s: str) -> int:
    d = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}

    nums_array = [x for x in s]
    i = 0
    r = 0
    while i < len(nums_array):
        if i == len(nums_array) - 1:
            r += d[nums_array[i]]
        elif d[nums_array[i]] >= d[nums_array[i + 1]]:
            r += d[nums_array[i]]
        else:
            r += d[nums_array[i + 1]] - d[nums_array[i]]
            i += 1
        i += 1

    return r


@benc_time
def romanToInt_two(s: str) -> int:
    d = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}

    res = 0
    prev = 1001

    for c in s:
        res += d[c]
        if prev < d[c]:
            res -= 2 * prev

        prev = d[c]

    return res


print(romanToInt_two("LVIII"))
