from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True

def main():
    s = Solution()

    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    result = s.isToeplitzMatrix(matrix)
    print(f"{result}")

if __name__ == '__main__':
    main()
