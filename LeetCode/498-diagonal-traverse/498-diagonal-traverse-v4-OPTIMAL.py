from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        result = []
        i = j = 0

        for _ in range(n * m):
            result.append(mat[i][j])

            if (i + j) & 1 == 0: # even
                if j == m - 1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else: # odd
                if i == n - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i +=1
                    j -= 1

        return result

def main():
    s = Solution()

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    result = s.findDiagonalOrder(mat)
    print(f"{result=}")

if __name__ == '__main__':
    main()
