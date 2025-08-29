from typing import List

class Solution:
    def printMatrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            for val in row:
                print(val, end=' ')
            print()
        print()

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])

        for i in range(0, n):
            if not all(matrix[i][0] == matrix[i + j][j] for j in range(0, min(m, n - i))):
                return False

        for j in range(1, m):
            if not all(matrix[0][j] == matrix[i][j + i] for i in range(0, min(n, m - j))):
                return False

        return True

def main():
    s = Solution()

    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    result = s.isToeplitzMatrix(matrix)
    print(f"{result}")

if __name__ == '__main__':
    main()
