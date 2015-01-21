#!/usr/bin/env python


def fibonacchi(n):
	"""
	Returns the n'th number of the fibonacchi sequence.
	Unless n is negative, then None is returned.
	"""
	if n < 0:
		return None
	elif n == 0:
		return 0
	elif n == 1:
		return 1 
	return fibonacchi(n-1) + fibonacchi(n-2)


def lucas(n):
	"""
	Returns the n'th number of the Lucas sequence.
	Unless n is negative, then None is returned.
	"""
	if n < 0:
		return None
	elif n == 0:
		return 2
	elif n == 1: 
		return 1			
	return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0, y=1):
	"""	
	sum_series requires one paramater by default, and will return the n'th value of
	the fibonacchi series. If you supply two extra parameters, for example sum_series(3, 2, 1), 
	then sum_series returns the n'th value of the lucas series.
	"""

	if x == 0 and y == 1:
		return fibonacchi(n)
	elif x == 2 and y == 1:
		return lucas(n)
	else:
		return None

if __name__ == "__main__":
	# Runing a few tests
	assert fibonacchi(-2) == None
	assert fibonacchi(1) == 1
	assert fibonacchi(0) == 0
	assert fibonacchi(7) == 13	

	assert lucas(-2) == None
	assert lucas(0) == 2
	assert lucas(1) == 1
	assert lucas(2) == 3
	assert lucas(3) == 4 
	assert lucas(4) == 7
