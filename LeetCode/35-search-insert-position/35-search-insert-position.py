from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums)
        while a < b:
            m = (a + b) // 2

            if nums[m] < target:
                a = m + 1
            else:
                b = m
        return a