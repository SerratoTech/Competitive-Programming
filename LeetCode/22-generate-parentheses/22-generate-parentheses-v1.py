from sys import stdin
from typing import List

def readLine():
    return stdin.readline().strip()

def readInt():
    return int(readLine())

def readInts():
    return list(map(int, readLine().split()))

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for symbol in s:
            if symbol == '(':
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                
                if  symbol == ")" and top != "(":
                    return False

        return len(stack) == 0

    def generateCombination(self, i: int, n: int, remaining_open_parenthesis: int, result: List[str], combination: str = ''):
        if i == n:
            if self.isValid(combination):
                result.append(combination)
            return
        
        if remaining_open_parenthesis > 0:
            self.generateCombination(i + 1, n, remaining_open_parenthesis - 1, result, combination + '(')
        self.generateCombination(i + 1, n, remaining_open_parenthesis, result, combination + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateCombination(0, 2 * n, n, result)
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