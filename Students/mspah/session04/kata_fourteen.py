#!/usr/bin/env python

import string

def main():


	try:
		f = open('sherlock_small.txt')
	except IOerror:
		print "Couldn't open sherlock_small.txt"

	print create_trigram_dictonary(f)

def create_trigram_dictonary(f):

	trigram = {}
	table = string.maketrans("","")

	for line in f.readlines():
		line = remove_punctuation(line, table).split()
		print line

		for x in xrange(len(line)):
			key = line[x] + line[x+1]
			trigram[key] = line[x+2]


def remove_punctuation(line, table):
	return line.translate(table, string.punctuation)



if __name__ == "__main__":
	main()