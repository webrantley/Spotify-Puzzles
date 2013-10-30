import sys

def reverse(integer):
	rev = 0
	temp = bin(integer)[2:]
	for i in range(len(temp)): #read from l to r instead of reversing string
		if temp[i] == '1':
			rev += 2**i
	return rev

def main():
	"""Solution to Spotify Puzzle reversebinary"""
	for line in sys.stdin:
		print(reverse(int(line)))

if __name__ == '__main__':
	main()