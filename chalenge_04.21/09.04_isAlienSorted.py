# Verifying an Alien Dictionary
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien language.

from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    if len(words) == 1:
        return True

    order_arr = {x: i for i, x in enumerate(order)}

    last = words[0]
    for i in range(1, len(words)):
        for j in range(len(last)):
            if j >= len(words[i]): return False

            if words[i][j] != last[j]:
                if order_arr[words[i][j]] < order_arr[last[j]]:
                    return False
                else:
                    f = False
                    break

        last = words[i]

    return True


print(isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
