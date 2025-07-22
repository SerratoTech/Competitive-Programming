from sys import stdin

def readLine():
	return stdin.readline().strip()

def readInt():
	return int(readLine())

def readInts():
	return list(map(int, readLine().split()))

NOT_FOUND = -1

def find_words(s: str) -> int:
	pos_fft = s.find('FFT')
	pos_ntt = s.find('NTT')
	return pos_fft if pos_fft != NOT_FOUND else pos_ntt

def make_it_non_difficult(s: str) -> str:
	l = list(s)
	l.sort()
	first_part = list(filter(lambda c: c == 'T', l))
	second_part = list(filter(lambda c: c != 'T', l))
			
	return ''.join(first_part + second_part)

def main():
	T = readInt()
	for t in range(T):
		s = readLine()
		if find_words(s) == NOT_FOUND:
			print(s)
		else:
			ans = make_it_non_difficult(s)
			print(ans)

if __name__ == '__main__':
	main()
