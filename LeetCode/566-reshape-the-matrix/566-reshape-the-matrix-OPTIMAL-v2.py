from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        if r * c != n * m:
            return mat

        k = 0
        result = []

        for i in range(r):
            result.append([])

            for j in range(c):
                k = (i * c) + j
                result[i].append(mat[k // m][k % m])

        return result

def main():
    s = Solution()

    result = s.matrixReshape([[1, 2], [3, 4]], 1, 4)

    print(result)

if __name__ == '__main__':
    main()
