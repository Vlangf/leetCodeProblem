# 1710. Maximum Units on a Truck
# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
# where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.
from typing import List
from random import randint as rnd


def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1])
    units = 0
    while truckSize and boxTypes:
        boxes = boxTypes.pop()
        if truckSize > boxes[0]:
            units += boxes[1] * boxes[0]
            truckSize -= boxes[0]
        else:
            units += boxes[1] * truckSize
            break

    return units


arr = [[rnd(1, 1001), rnd(1, 1001)] for _ in range(1001)]

print(maximum_units(boxTypes=arr, truckSize=99999))
