# 867. Transpose Matrix
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    result = []

    for i in range(len(matrix[0])):
        a = []
        for j in range(len(matrix)):
            a.append(matrix[j][i])
        result.append(a)

    return result


def transpose_two(matrix: List[List[int]]) -> List[List[int]]:
    result = list(map(list, zip(*matrix)))


    return result


print(transpose_two(matrix=[[1,2,3],[4,5,6],[7,8,9]]))
