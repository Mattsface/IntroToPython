

def swap_string(string):
	fc = string[0:1]
	lc = string[len(string)-1:]
	center = string[1:(len(string)-1)]

	return lc + center + fc

	# return val[-1] + val[1:-1] + val[0]

def remove_every_other_c(string):
	return string[::2]


def first4_last4(string):
	first4 = string[0:4]
	last4 = string[-4:]
	center = string[4:-4]
	# return string[4:-4:2]


if __name__ == "__main__":
	string = "this is my string"
	print swap_string(string)
	print remove_every_other_c(string)