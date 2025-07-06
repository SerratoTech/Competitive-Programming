class Solution:
    def mySqrt(self, x: int) -> int:
        a, b = 0, x // 2 + 1
        while a < b:
            m = (a + b) // 2

            if m * m < x:
                a = m + 1
            else:
                b = m
        return a if a * a == x else a - 1