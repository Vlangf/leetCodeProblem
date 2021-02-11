# Count and Say
# Solution
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of groups so that each group
# is a contiguous section all of the same character. Then for each group, say the number of characters,
# then say the character. To convert the saying into a digit string, replace the counts with a number and
# concatenate every saying.


def count_and_say(n: int) -> str:
    say = '1'
    for i in range(n-1):
        arr = []
        for each in say:
            if arr and arr[-1][-1] == each:
                arr[-1].append(each)
            else:
                arr.append([each])
        say = ''.join([str(len(x)) + x[0] for x in arr])

    return say


print(count_and_say(4))
