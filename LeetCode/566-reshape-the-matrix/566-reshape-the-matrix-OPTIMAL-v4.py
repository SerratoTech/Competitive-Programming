from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m, k = len(mat), len(mat[0]), 0

        if (n * m) != (r * c):
            return mat
        
        flat = [val for row in mat for val in row]
        result = [flat[i * c : (i + 1) * c] for i in range(r)]
        return result

def main():
    s = Solution()

    result = s.matrixReshape([[1, 2], [3, 4]], 1, 4)

    print(result)

if __name__ == '__main__':
    main()
