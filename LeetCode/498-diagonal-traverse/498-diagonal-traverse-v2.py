from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        result = []
        goUp = True
        i, j = 0, 0

        while i != n and j != m:
            result.append(mat[i][j])

            if goUp and not (i == 0 or j == (m - 1)):
                i -= 1
                j += 1
            elif not goUp and not (i == (n - 1) or j == 0):
                i += 1
                j -= 1
            elif i == 0 or j == (m - 1):
                goUp = not goUp

                if j == (m - 1):
                    i += 1
                else:
                    j += 1
            elif i == (n - 1) or j == 0:
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
