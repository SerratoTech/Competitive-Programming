from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        startY, endY = 0, m
        startX, endX = 0, n
        result = []

        while (endY - startY) >= 1 and (endX - startX) >= 1:
            for i in range(startX, endX):
                result.append(matrix[startY][i])
            
            if (endY - startY) == 1:
                break

            for i in range(startY + 1, endY):
                result.append(matrix[i][endX - 1])
            
            if (endX - startX) == 1:
                break

            for i in range(endX - 2, startX - 1, -1):
                result.append(matrix[endY - 1][i])

            for i in range(endY - 2, startY, -1):
                result.append(matrix[i][startX])

            startY += 1
            endY -= 1
            startX += 1
            endX -= 1

        return result

def main():
    s = Solution()

    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # spiral_list = s.spiralOrder(matrix)
    # print(spiral_list)

    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # spiral_list = s.spiralOrder(matrix)
    # print(spiral_list)

    matrix = [[2,5,8],[4,0,-1]]
    spiral_list = s.spiralOrder(matrix)
    print(spiral_list)

if __name__ == '__main__':
    main()
