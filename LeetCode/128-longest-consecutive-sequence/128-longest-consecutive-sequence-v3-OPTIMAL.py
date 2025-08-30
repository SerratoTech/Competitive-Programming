from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return 1

        result = 1
        number_set = set(nums)

        for num in number_set:
            if num - 1 not in number_set:
                sequence = 1
                while num + sequence in number_set:
                    sequence += 1
                result = max(result, sequence)
        
        return result

def main():
    s = Solution()
    
    nums = [100, 4, 200, 1, 3, 2]
    result = s.longestConsecutive(nums)
    print(f"{result=}")

if __name__ == '__main__':
    main()