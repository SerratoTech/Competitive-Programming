from typing import List
from collections import Counter

def printList(list: list):
    print(' '.join(str(x) for x in list))

# Using Counter from collections (Hash Table) - Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 2
        counter = Counter(nums)

        for num, count in counter.items():
            if count > m:
                return num

        return nums[0]

def main():
    nums = [2,2,1,1,1,2,2]
    printList(nums)
    solution = Solution()
    ans = solution.majorityElement(nums)
    print('Answer: %d' % ans)

if __name__ == '__main__':
    main()