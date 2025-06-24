from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

            if freq[num] > 1:
                return True

        return False