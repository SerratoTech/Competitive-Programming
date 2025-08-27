from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])

        result = []
        for j in range(m):
            result.append([])

            for i in range(n):
                result[j].append(matrix[i][j])

        return result
