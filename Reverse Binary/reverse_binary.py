import sys

if __name__ == "__main__":
	for line in sys.stdin:
		print(int(bin(int(line))[2:][::-1], 2))