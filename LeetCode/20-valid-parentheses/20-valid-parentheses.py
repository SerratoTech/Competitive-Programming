from sys import stdin

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
            if symbol in "({[":
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                
                if  symbol == ")" and top != "(" or \
                    symbol == "}" and top != "{" or \
                    symbol == "]" and top != "[":
                    return False

        return len(stack) == 0

def main():
    print("Input:", end=" ", flush=True)
    inpur = readLine()
    solution = Solution()
    result = solution.isValid(inpur)
    print("Output:", result)
if __name__ == "__main__":
    main()