#!/usr/bin/env python

import sys

DONERS = [	("matt", [ 2, 4 ]),
			("kelly", [ 1, 2, 3]),
			("tom", [ 2, 4 ]), 
			("mitch", [ 3, 5, 6 ]),
			("lisa", [ 3, 4, 3 ])
			]

def main_menu():
	print ""
	print "What would you like to do?"
	print "1. Send a Thank You"
	print "2. Create a report"
	print "3. Exit"
	result = raw_input("Please choose 1, 2 or 3: ")
	
	if result == "1" or result == "2" or result == "3":
		return result
	else:
		main_menu()


def thank_you_list():
	print ""
	print "Please review the following choices"
	print "To list doners: type list"
	print "To add a new doner: type the doners name"
	print "To add a new donation to an existing doner, type the doners name"
	result = raw_input("What do you want to do? ").lower()

	if result == "list":
		print_doners()
		thank_you_list()
			
	for doner in DONERS:
		if result == doner[0]:	
			donation(result)
	else:
		DONERS.append((result, []))
		donation(result)
		

def donation(user):
	print ""


	try:
		amount = int(raw_input("How much would like to donate %s? " % user))
		
		for doner in DONERS:
			if doner[0] == user:
				doner[1].append(amount)
			else:
				continue
	except ValueError:
		print "Donation must be a integer"
		donation(user)
		
	thank_you_email(user, amount)



def print_doners():
	print ""
	for doner in DONERS:
		print doner[0]


def thank_you_email(user, amount):
	print ""
	print ""
	print "to: %s@gmail.com" % user
	print ""
	print "Thank you for your donation %s" % user
	print "The amount of %i will help dearly" % amount
	print ""
	print "Thanks,"
	print "      Matthew Spah"
	main()

def create_report():
	for doner in DONERS:
		name = doner[0]
		donations = doner[1]
		average, total, total_donations = calc_average(donations)
		print "Donater: %s Average Donation: %.02f Total Amount: %i Total Donations: %i" % (name, average, total_donations, total )
	main()


def calc_average(donations):
	total_donations = 0.0
	total = len(donations)
	for n in donations:
		total_donations = n + total_donations
		
	average = total_donations / total
	return average, total, int(total_donations) 



def main():
	result = main_menu()
	if result == "1":
		thank_you_list()
	elif result == "2":
		create_report()
	elif result == "3":
		sys.exit



if __name__ == '__main__':
	main()




