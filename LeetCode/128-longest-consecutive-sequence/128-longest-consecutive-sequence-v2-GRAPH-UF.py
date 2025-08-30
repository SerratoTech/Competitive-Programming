from typing import List, DefaultDict
from collections import defaultdict

class Solution:
    def find_parent(self, parent: DefaultDict[int, int], node: int) -> int:
        if parent[node] != node:
            parent[node] = self.find_parent(parent, parent[node])
        return parent[node]

    def union(self, parent: DefaultDict[int, int], rank: DefaultDict[int, int], node_x: int, node_y: int) -> int:
        root_x = self.find_parent(parent, node_x)
        root_y = self.find_parent(parent, node_y)

        if root_x == root_y:
            return rank[root_x]

        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
            rank[root_x] += rank[root_y]
            return rank[root_x]

        parent[root_x] = root_y
        rank[root_y] += rank[root_x]
        return rank[root_y]

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return 1

        parent = defaultdict(int)
        rank = defaultdict(int)
        result = 1

        for num in nums:
            if num not in parent:
                parent[num] = num
                rank[num] += 1

        for num in nums:
            if num + 1 in parent:
                sequence = self.union(parent, rank, num, num + 1)
                result = max(result, sequence)

        return result

def main():
    s = Solution()
    
    # nums = [100, 4, 200, 1, 3, 2]
    # result = s.longestConsecutive(nums)
    # print(f"{result=}")

    nums = [0,3,7,2,5,8,4,6,0,1]
    result = s.longestConsecutive(nums)
    print(f"{result=}")

if __name__ == '__main__':
    main()