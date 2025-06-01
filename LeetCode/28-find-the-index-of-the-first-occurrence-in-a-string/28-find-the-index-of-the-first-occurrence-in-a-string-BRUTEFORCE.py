class Solution:
    NOT_FOUND = -1

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m > n:
            return self.NOT_FOUND

        for i in range(n - m + 1):
            pos = i
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    pos = self.NOT_FOUND
                    break
            if pos != self.NOT_FOUND:
                return pos

        return self.NOT_FOUND

def main():
    print('Find the index of the first occurrence in a string\n')
    string = input('String: ')
    pattern = input('Pattern: ')
    solution = Solution()
    ans = solution.strStr(string, pattern)
    print('Answer: {}'.format(ans))

if __name__ == '__main__':
    main()