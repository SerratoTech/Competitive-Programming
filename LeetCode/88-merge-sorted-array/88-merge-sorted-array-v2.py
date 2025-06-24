from sys import stdin
from typing import List

def readLine() -> str:
    return stdin.readline().strip()

def mapInts(line: str) -> list:
    return list(map(int, line.split()))

def readInts() -> list:
    return mapInts(readLine())

def printList(l: list):
    print(' '.join(str(x) for x in l))

class Solution:
    def rotate_left(self, list: List, rotations: int):
        n = len(list)
        rotations %= n

        def reverse(start: int, end: int):
            while start < end:
                list[start], list[end] = list[end], list[start]
                start += 1
                end -= 1

        reverse(0, rotations - 1)
        reverse(rotations, n - 1)
        reverse(0, n - 1)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = 0, 0, m % (n + m)
        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    nums1[k] = nums1[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            elif i < m:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k = (k + 1) % (n + m)

        self.rotate_left(nums1, m)

def main():
    print('Merge Sorted Array\n')

    m = int(input('m: '))
    print('>> m: %d\n' % m)

    line = input('nums1: ')
    nums1 = mapInts(line)

    print('>> nums1: {}\n'.format(' '.join(str(x) for x in nums1)))

    n = int(input('n: '))
    print('>> n: %d\n' % n)

    line = input('nums2: ')
    nums2 = mapInts(line)
    print('>> nums2: {}\n'.format(' '.join(str(x) for x in nums2)))

    # Add extra spaces for 'nums2' elements.
    nums1.extend([0 for i in range(n)])

    print('>> New nums1: {}\n'.format(' '.join(str(x) for x in nums1)))

    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    print('Answer: {}'.format(' '.join(str(x) for x in nums1)))

if __name__ == '__main__':
    main()
