from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m, k = len(mat), len(mat[0]), 0

        if (r * c) != (n * m):
            return mat

        result = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(n):
            for j in range(m):
                result[k // c][k % c] = mat[i][j]
                k += 1
    
        return result
