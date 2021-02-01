# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).
from metrics import benc_time


@benc_time
def hamming_weight(n: int) -> int:
    weight = 0
    while n:
        d = n % 2
        if d == 1:
            weight += 1
        n //= 2

    return weight


@benc_time
def hamming_weight_two(n: int) -> int:
    return bin(n).count('1')


@benc_time
def hamming_weight_three(n: int) -> int:
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c


@benc_time
def hamming_weight_four(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n >>= 1

    return res


print(hamming_weight_three(int('000000100',
                             2)))
