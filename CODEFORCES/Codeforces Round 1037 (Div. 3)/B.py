from sys import stdin

def readLine():
    return stdin.readline().strip()

def readInt():
    return int(readLine())

def readInts():
    return list(map(int, readLine().split()))

def main():
    t = readInt()

    for i in range(t):
        n, k = readInts()
        a = readInts()

        j, ans = 0, 0
        while j < n - k + 1:
            if all(aj == 0 for aj in a[j : j + k]):
                ans += 1
                j += k
            j += 1
        print(ans)

if __name__ == '__main__':
    main()