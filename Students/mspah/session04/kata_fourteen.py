#!/usr/bin/env python

def main():
	try:
		f = open('sherlock_small.txt')
	except IOerror:
		print "Couldn't open sherlock_small.txt"

	create_traigram_dictonary(f)

def create_traigram_dictonary(f):

	for line in f:
		print line





if __name__ = "__main__":
	main()