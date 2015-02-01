#!/usr/bin/env python


def main():
	part_1()
	part_2()
	part_3()
	part_4()
	part_5()



def part_1():
	'''
	Dictionary lab main function
	'''

	labdict = { "name": "Chris", "city": "Seattle", "cake": "Chocolate"}

	print labdict

	labdict.pop("cake")

	print labdict

	labdict["fruit"] = "Mango"

	print labdict.keys()
	print labdict.values()

	if "cake" in labdict:
		print "Cake is present"

	for key, value in labdict.items():
		if value == "Mango":
			print "Mango is present"

def part_2():
	'''
	Create two arrays and create a dictonary using dict and zip
	'''
	n = [ x for x in range(15+1)]
	h = [ hex(x) for x in range(15+1)]

	print dict(zip(n, h))

def part_3():
	labdict = { "name": "Chris", "city": "Seattle", "cake": "Chocolate"}

	for key, value in labdict.items():
		t = value.count('t')
		labdict[key] = t
	else:
		print labdict

def part_4():

	s2 = set([ x for x in range(21) if x % 2 == 0])
	s3 = set([ x for x in range(21) if x % 3 == 0])
	s4 = set([ x for x in range(21) if x % 4 == 0])
	print s2
	print s3
	print s4

	print s3.issubset(s2)
	print s4.issubset(s2)

def part_5():
	set_python = set([ x for x in "Python"])
	set_python.update("i")
	
	frozen_set = frozenset([x for x in "marathon"])

	print set_python.union(frozen_set)
	print set_python.intersection(frozen_set)

	


if __name__ == "__main__":
	main()
