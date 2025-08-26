from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        startY, endY = 0, n
        startX, endX = 0, n
        idx = 1

        while (endY - startY) >= 1 and (endX - startX) >= 1:
            for i in range(startX, endX):
                matrix[startY][i] = idx
                idx += 1
            
            if (endY - startY) == 1:
                break
            
            for i in range(startY + 1, endY):
                matrix[i][endX - 1] = idx
                idx += 1
            
            if (endX - startX) == 1:
                break
            
            for i in range(endX - 2, startX - 1, -1):
                matrix[endY - 1][i] = idx
                idx += 1
            
            for i in range(endY - 2, startY, -1):
                matrix[i][startX] = idx
                idx += 1
            
            startY += 1
            endY -= 1
            startX += 1
            endX -= 1
        
        return matrix

def main():
    s = Solution()

    result = s.generateMatrix(3)
    print(result)

if __name__ == '__main__':
    main()
