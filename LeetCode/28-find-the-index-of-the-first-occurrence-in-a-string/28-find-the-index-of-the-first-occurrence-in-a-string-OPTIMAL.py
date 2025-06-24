def printStringAsList(str: list, n: int):
    for i in range(n):
        print(f"{i:>2}" if i == 0 else f" {i:>2}", end='')
    print()

    for i in range(n):
        print('{:>2}'.format(str[i]) if i == 0 else ' {:>2}'.format(str[i]), end='')
    print('\n')

class Solution:
    NOT_FOUND = -1

    def LPS(self, needle: str, m: int) -> list:
        prefixes = [0 for i in range(m)]

        i, j = 1,  0
        while i < m:
            while j > 0 and needle[i] != needle[j]:
                j = prefixes[j - 1]
            if needle[i] == needle[j]:
                j += 1
            prefixes[i] = j
            i += 1

        return prefixes

    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if m > n:
            return self.NOT_FOUND

        prefixes = self.LPS(needle, m)

        i, j = 0, 0
        while i < n:
            while j > 0 and haystack[i] != needle[j]:
                j = prefixes[j - 1]
            if haystack[i] == needle[j]:
                j += 1 
            i += 1
            if j == m:
                return i - m 

        return self.NOT_FOUND

def main():
    print('Find the index of the first occurrence in a string\n')
    string = input('String: ')
    print('\n>> String: %s' % string)
    pattern = input('Pattern: ')
    print('\n>> pattern: %s' % pattern)
    solution = Solution()
    ans = solution.strStr(string, pattern)
    print('Answer: {}'.format(ans))

if __name__ == '__main__':
    main()