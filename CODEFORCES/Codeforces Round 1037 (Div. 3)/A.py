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
        x = readLine()
        y = min(list(x))
        print(y)

if __name__ == '__main__':
    main()