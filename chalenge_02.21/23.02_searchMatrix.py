# Search a 2D Matrix II
# Write an efficient algorithm that searches for a target value in an m x n integer matrix.
# The matrix has the following properties:
#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.
from typing import List
from metrics import benc_time


@benc_time
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    r, c = 0, 0
    r_l, c_l = len(matrix), len(matrix[0])
    while r_l > r and c_l > c:
        if matrix[r][c] == target:
            return True
        elif (c == len(matrix[0]) - 1) or (matrix[r][c] > target):
            c = 0
            r += 1
        else:
            c += 1

    return False


def searchMatrix_two(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    columns = len(matrix[0])
    row = 0
    col = columns - 1
    while col < columns and row < rows:
        if matrix[row][col] == target:
            return True

        if target > matrix[row][col]:
            row += 1

        else:
            col -= 1

    return False


print(searchMatrix(
    matrix=[[-5]], target=-10

))
