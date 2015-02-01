#!/usr/bin/env python
def main():
	try:
		f = open('students.txt')
	except IOerror:
		print "Couldn't open students.txt"


	languages = collect_languages(f)
	
	for language in languages:
		print language


def collect_languages(f):
	l = []

	for line in f.readlines():
		words = line.rstrip().split(":")
		for languages in words[1].split(','):
			l.append(languages.strip())
		
	return set(l)




if __name__ == "__main__":
	main()