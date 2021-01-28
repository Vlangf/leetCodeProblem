# 1736. Latest Time by Replacing Hidden Digits
# You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?)
# The valid times are those inclusively between 00:00 and 23:59.
# Return the latest valid time you can get from time by replacing the hidden digits

# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
from metrics import benc_time
import memory_profiler


@benc_time
@memory_profiler.profile
def maximum_time(time: str) -> str:
    latest_time = []
    if time[0] == '?':
        latest_time.append('2')
    else:
        latest_time.append(time[0])

    if time[1] == '?':
        if int(latest_time[0]) > 1:
            latest_time.append('3')
        else:
            latest_time.append('9')
    else:
        latest_time.append(time[1])

    if time[3] == '?':
        latest_time.append('5')
    else:
        latest_time.append(time[3])

    if time[4] == '?':
        latest_time.append('9')
    else:
        latest_time.append(time[4])

    latest_time.insert(2, ':')

    return ''.join(latest_time)


@benc_time
def maximum_time_two(time: str) -> str:
    i_dict = {0: '2', 1: '9', 3: '5', 4: '9'}
    if time[0] == '2':
        i_dict[1] = '3'

    if time[0] == '?' and time[1] != '?' and int(time[1]) > 3:
        i_dict[0] = '1'

    for i in range(len(time)):
        if time[i] == '?':
            time = time.replace('?', i_dict[i], 1)
            if i == 0:
                i_dict[1] = '3'

    return time


@benc_time
def maximum_time_three(time: str) -> str:
    max_time = '23:59' if time[0] in '?2' and time[1] in '?0123' else '19:59'
    return ''.join(x if x != '?' else y for x, y in zip(time, max_time))


print(maximum_time_two('1?:22'))
