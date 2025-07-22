from sys import stdin
from math import gcd
 
def readLine():
	return stdin.readline().strip()
 
def readInt():
	return int(readLine())
 
def readInts():
	return list(map(int, readLine().split()))
 
NOT_FOUND = -1
 
def go_to_origin(x: int, y: int, k: int) -> int:
	g = gcd(x, y)
	return 1 if (x // g) <= k and (y // g) <= k else 2
 
def main():
	T = readInt()
	for t in range(T):
		a, b, k = readInts()
		ans = go_to_origin(a, b, k)
		print(ans)
 
if __name__ == '__main__':
	main()