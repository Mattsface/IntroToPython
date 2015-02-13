#!/usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

[2520, 1260, 840, 630, 504, 420, 360, 315, 280, 252]

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""



def main():
    i = 1
    while True:
        if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0 and i % 10 != 0:
            print i
        else:
            i += 1

    print i


if __name__ == "__main__":
    main()