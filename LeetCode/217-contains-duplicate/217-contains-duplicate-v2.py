from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        return any(nums[i] == nums[i + 1] for i in range(n - 1))