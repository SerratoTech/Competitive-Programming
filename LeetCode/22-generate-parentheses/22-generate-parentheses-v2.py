from sys import stdin
from typing import List

def readLine():
    return stdin.readline().strip()

def readInt():
    return int(readLine())

def readInts():
    return list(map(int, readLine().split()))

class Solution:
    def generateCombination(self, n: int, result: List[str], left: int = 0, right: int = 0, combination: str = ''):
        if right == n:
            result.append(combination)
            return

        if left < n:
            self.generateCombination(n, result, left + 1, right, combination + '(')
        
        if right < left:
            self.generateCombination(n, result, left, right + 1, combination + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateCombination(n, result)
        return result

def main():
    print("Input:", end=" ", flush=True)
    n = readInt()
    solution = Solution()
    result = solution.generateParenthesis(n)
    print("Output:", result)
    print("No. of Combinations:", len(result))

if __name__ == "__main__":
    main()