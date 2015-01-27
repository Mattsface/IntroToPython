#!/usr/bin/env python



def list_lab_part1(fruits):
	print fruits
	new_fruit = raw_input("Which fruit would you like to add? ")
	fruits.append(new_fruit)
	print fruits
	number = int(raw_input("What fruit would like to see? (provide an interger) "))
	print "The number %i fruit is %s" % (number, fruits[(number - 1)])
	fruits += [ "Grapes" ]
	print fruits
	fruits.insert(0, "Tomato")
	print fruits

	for fruit in fruits:
		if fruit[0] == "P":
			print fruit

	return fruits


def remove_from_list(fruits, item):

	try:
		fruits.remove(item)
	except:
		print "Fruit not found"
		item = raw_input("What fruit do you want to remove? ")
		remove_from_list(fruits, item)


def list_lab_part2(fruits):
	print fruits
	fruits.pop()
	print fruits
	item = raw_input("What fruit do you want to remove? ")
	remove_from_list(fruits, item)
	print fruits

def list_lab_part3(fruits):
	for fruit in fruits:
		while True:
			answer = raw_input("Do you like %s? yes or no? " % fruit.lower())
			if answer == "yes":
				break
			elif answer == "no":
				fruits.remove(fruit)
				break
	print fruits



if __name__ == "__main__":
	fruits = ["Apples", "Pears", "Oranges", "Peaches"]
	fruits = list_lab_part1(fruits)
	list_lab_part2(fruits)
	list_lab_part3(fruits)