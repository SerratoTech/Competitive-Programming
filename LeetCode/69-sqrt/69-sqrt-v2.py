class Solution:
    def mySqrt(self, x: int) -> int:
        s, x = x, x // 2 + 1
        while x * x > s:
            x = (x + s // x) // 2
        return x

def main():
    num = 20
    solution = Solution()
    print("SQRT({}) = {}.".format(num, solution.mySqrt(num)))

if __name__ == '__main__':
    main()