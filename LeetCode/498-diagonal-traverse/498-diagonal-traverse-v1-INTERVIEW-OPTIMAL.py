from typing import List

class Solution:
    def isFinalCell(self, n: int, m: int, i: int, j: int):
        return i == n or j == m
    
    def isOnTopOrRightEdge(self, m: int, i: int, j: int) -> bool:
        return i == 0 or j == (m - 1)
    
    def isOnBottomOrLeftEdge(self, n: int, i: int, j: int) -> bool:
        return i == (n - 1) or j == 0

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        result = []
        goUp = True
        i, j = 0, 0

        while not self.isFinalCell(n, m, i, j):
            result.append(mat[i][j])

            if goUp and not self.isOnTopOrRightEdge(m, i, j):
                i -= 1
                j += 1
            elif not goUp and not self.isOnBottomOrLeftEdge(n, i, j):
                i += 1
                j -= 1
            elif self.isOnTopOrRightEdge(m, i, j):
                goUp = not goUp

                if j == (m - 1):
                    i += 1
                else:
                    j += 1
            elif self.isOnBottomOrLeftEdge(n, i, j):
                goUp = not goUp

                if i == (n - 1):
                    j += 1
                else:
                    i += 1

        return result

def main():
    s = Solution()

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    result = s.findDiagonalOrder(mat)
    print(f"{result=}")

if __name__ == '__main__':
    main()
