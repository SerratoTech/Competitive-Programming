from sys import stdin
from bisect import bisect_right

def readLine():
    return stdin.readline().strip()

def readInt():
    return int(readLine())

def readInts():
    return list(map(int, readLine().split()))

def main():
    t = readInt()

    for t in range(t):
        n, c = readInts()
        a = readInts()
        a.sort()
        ans = 0

        for i in range(n):
            pos = bisect_right(a, c)
            bag_weight = a[pos - 1]
            ans += 0 if bag_weight <= c else 1
            a.pop(pos - 1)
            a = list(map(lambda x: 2 * x, a))

        print(ans)

if __name__ == '__main__':
    main()