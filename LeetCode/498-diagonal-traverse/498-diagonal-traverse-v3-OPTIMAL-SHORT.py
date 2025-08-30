from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        bucket = [[] for _ in range(n + m - 1)]
        result = []

        for i in range(n):
            for j in range(m):
                bucket[i + j].append(mat[i][j])

        for i in range(n + m - 1):
            row = bucket[i] if i & 1 == 1 else reversed(bucket[i])
            for val in row:
                result.append(val)

        return result

def main():
    s = Solution()

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    result = s.findDiagonalOrder(mat)
    print(f"{result=}")

if __name__ == '__main__':
    main()
