# Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
# you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps(num: int) -> int:
    count = 0
    while num != 0:
        if num % 2:
            num -= 1
        else:
            num //= 2

        count += 1

    return count


print(numberOfSteps(1000000))
