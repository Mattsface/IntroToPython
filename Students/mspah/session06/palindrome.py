#!/usr/bin/env python

"""
A palindromic number reads the same both ways.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys

def main():

    x = 100
    y = 100
    large_pn = 0


    for x in range(100, 999):
        for y in range(100, 999):
            pn = x * y
            if check_pn(pn):
                if pn > large_pn:
                    large_pn = pn

    print large_pn

def check_pn(pn):
    pn_string = str(pn)
    if not len(pn_string) % 2:
        split = len(pn_string)
        split /= 2
        front = pn_string[split:]
        rear = pn_string[:split]
        rear = rear[::-1]
        if front == rear:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    main()


