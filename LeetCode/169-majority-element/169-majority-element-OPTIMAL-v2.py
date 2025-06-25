from typing import List

def printList(list: list):
    print(' '.join(str(x) for x in list))

# Boyer-Moore Voting Algorithm - Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
        # Strict Solution (majority element check):
        # Verify if the candidate is indeed the majority element
        # return candidate if nums.count(candidate) > len(nums) // 2 else None

def main():
    nums = [2,2,1,1,1,2,2]
    printList(nums)
    solution = Solution()
    ans = solution.majorityElement(nums)
    print('Answer: %d' % ans)

if __name__ == '__main__':
    main()