#!/usr/bin/env python


def main():

    list1 = [ 'John', 'Gary, Sam, Paul', 'Mary, Frank', 'Smith', 'Ron, Bill, Don' ]
    list2 = []

    for item in list1:
        if ',' in item:
            list2.append(item.split(','))
        else:
            list2.append(item)
    print [item for list2 in list2 for item in list2]





if __name__ == "__main__":
    main()ßßsß