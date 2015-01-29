#!/usr/bin/env python




# Use a nested list to hold customer information and how much they have donated 

# create a function that creates the menu

def main_menu():
	print ""
	print "What would you like to do?"
	print "1. Send a Thank You"
	print "2. Create a report"
	result = raw_input("Please choose 1 or 2 ")
	if result == "1" or result == "2":
		return result
	else:
		main_menu()

def main():
	doners = [ "matt" = [ 2, 4 ], "kelly" = [ 1, 2, 3], "tom" = [ 2, 4 ], "mitch" = [ 3, 5, 6 ], "lisa" = [ 3, 4, 3] ]











if __name__ == '__main__':