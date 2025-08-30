from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return 1

        is_consecutive = False
        sequence = 0
        result = 1
        nums.sort()

        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                continue
            elif nums[i - 1] + 1 == nums[i]:
                if is_consecutive:
                    sequence += 1
                else:
                    is_consecutive = True
                    sequence = 2
            else:
                is_consecutive = False
                sequence = 1
            
            result = max(result, sequence)

        return result

def main():
    s = Solution()
    
    nums = [100, 4, 200, 1, 3, 2]
    result = s.longestConsecutive(nums)
    print(f"{result=}")

if __name__ == '__main__':
    main()