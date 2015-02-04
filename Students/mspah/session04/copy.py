#!/usr/bin/env python
"""
script to copy a file to a new location
"""

import sys
import argparse


def main():
    args = parse_arguements()

    try:
        s = open(args.source)
    except IOError:
        print "Unable to open file %s" % args.source


    # fix this :O
    try:
        d = open(args.destination, 'w')
    except IOError:
        print "Unable to open destination file"

    write_file(s, d)

    s.close()
    d.close()


def write_file(s, d):
    for line in s:
        d.write(line)


def parse_arguements():
    parser = argparse.ArgumentParser(add_help=True, description="Get input file and outpuit location for copy of file",
    prog=sys.argv[0])

    parser.add_argument('-s', '--source', action='store', help="source file to copy", dest='source')

    parser.add_argument('-d', '--destination', action="store", help="Destination path", dest='destination')

    args = parser.parse_args()
    return args



if __name__ == "__main__":
    main()