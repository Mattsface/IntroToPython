#!/usr/bin/env python


def main():
    #l = [ x for x in range(1, 50, 2)]
    l = [1, 2, 3]
    print centered_average(l)
    print second_lowest_highest(l)

def centered_average(l):
    sorted_list = sorted(l)

    total = 0.0
    for x in sorted_list[1:-1]:
        total += x

    try:
        return total / len(l)
    except ZeroDivisionError:
        return "Can't divide by Zero, List must contain more integers > 0"


def second_lowest_highest(l):
    sorted_list = sorted(l)
    total = 0.0
    for x in (sorted_list[1:2] + sorted_list[-2:-1]):
        total += x

    try:
        return total / 2
    except ZeroDivisionError:
        return "Can't divide by Zero, List must contain more integers > 0"





if __name__ == "__main__":
    main()