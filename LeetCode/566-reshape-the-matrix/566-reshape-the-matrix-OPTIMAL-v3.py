from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if n * m != r * c:
            return mat

        it = (mat[i // m][i % m] for i in range(n * m))
        return [[next(it) for _ in range(c)] for _ in range(r)]