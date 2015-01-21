#!/usr/bin/env python



def main():
	print ack(3,0)
	print ack(3,1)
	print ack(3,2)
	print ack(3,3)
	print ack(3,4)

def ack(m,n): 
	if m == 0:
		 return n + 1
	if m > 0 and n == 0:
		return ack(m-1, 1)
	if m > 0 and n > 0:
		return ack(m-1, ack(m, n-1))


if __name__ == "__main__":
	main()