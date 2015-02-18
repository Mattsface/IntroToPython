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

    new_file_name = user_input()

    scrub_file(filename, new_file_name)


def user_input():
    print "New output filename? (leave blank if you want to overwrite current file)"
    new_file_name = raw_input(" ")
    return new_file_name


def scrub_file(filename, new_file_name):
    """
    scrub file of all leading and trailing whitespace
    :param filename:
    :param new_file_name:
    :return:
    """
    if new_file_name:
        old_file = open(filename, "r")
        new_file = []
        for line in map(str.strip, old_file):
            new_file.append(line)

        old_file.close()

        the_scrubbed_file = open(new_file_name, "w")

        for line in new_file:
            the_scrubbed_file.write(line + '\n')

        the_scrubbed_file.close()
    else:
        old_file = open(filename, "r")
        new_file = []
        for line in map(str.strip, old_file):
            new_file.append(line)

        old_file.close()

        the_scrubbed_file = open(filename, "w")

        for line in new_file:
            the_scrubbed_file.write(line + '\n')

        the_scrubbed_file.close()

if __name__ == "__main__":
    main()
