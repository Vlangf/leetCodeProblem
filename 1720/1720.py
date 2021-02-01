# 1720. Decode XORed Array
# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
# For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.
from typing import List
from metrics import benc_time


@benc_time
def decode(encoded: List[int], first: int) -> List[int]:
    encoded.insert(0, first)
    for i in range(1, len(encoded)):
        encoded[i] = encoded[i] ^ encoded[i - 1]

    return encoded


@benc_time
def decode_two(encoded: List[int], first: int) -> List[int]:
    arr = [first]
    for i in encoded:
        arr.append(i ^ arr[-1])

    return arr


print(decode_two(encoded=[1, 2, 3], first=4))
