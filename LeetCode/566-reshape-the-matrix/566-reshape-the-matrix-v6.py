from typing import List
from numpy import fromiter

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        
        if n * m != r * c:
            return mat

        arr = fromiter((val for row in mat for val in row), dtype=int, count=n*m)
        return arr.reshape(r, c).tolist()

def main():
    s = Solution()

    result = s.matrixReshape([[1, 2], [3, 4]], 1, 4)

    print(result)

if __name__ == '__main__':
    main()
