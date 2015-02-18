#!/usr/bin/env python

import sys
import os

def main():

    try:
        filename = sys.argv[1]
    except IndexError:
        print "Please supply a file name"
        sys.exit(1)

    if not os.path.isfile(filename):
        print "Unable to locate file %s" % filename
        sys.exit(1)

    overwrite = user_input()

    scrub_file(filename, overwrite)


def user_input():
    answer = raw_input("Do you want to overwrite the file Y/N ")
    if answer is "Y":
        return True
    elif answer is "N":
        return False
    else:
        print "Please answer with Y or N"
        user_input()

def scrub_file(filename, overwrite):
    new_file_name = filename + ".scrub"
    new_file = open(new_file_name, "w")

    file = open(filename, "r")

    for line in map(str.strip, file):
        print line


if __name__ == "__main__":
    main()
