#!/usr/bin/env python

def main():

    the_list = function_builder(5)
    print the_list[1](2)
    print the_list[2](2)

    for f in the_list:
        print f(5)


def function_builder(n):
    l = []

    for x in range(0, n):
        l.append(lambda y, e=x: e+y)

    return l

if __name__ == "__main__":
    main()