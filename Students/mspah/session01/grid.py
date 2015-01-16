


def print_grid(n):

	if n & 2 == 0:
		n = n + 1

	center =  ( n / 2 ) - 1 

	for line in range(n):
		if line==0 or line==(center + 1) or line==(n - 1):
			print '+',
			print '-' * center,
			print '+',
			print '-' * center,
			print '+'
		else:
			print '|',
			print " " * center,
			print '|',
			print " " * center,
			print "|"





def main():
	print_grid(16)


main()