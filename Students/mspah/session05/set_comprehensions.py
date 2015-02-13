#!/usr/bin/env python



def main():
    s2 = { s for s in range(0, 21, 2) }
    s3 = { s for s in range(0, 21, 3) }
    s4 = { s for s in range(0, 21, 4) }

    print s2
    print s3
    print s4

    n = 6
    divisors = range(2, n+1)
    sets = [ set() for x in divisors ]

    for d, s in zip(divisors, sets):
        print d
        print s
        [ s.add(x) for x in range(1, 21) if not x % d]

    print sets


    new_sets = [ { s for s in range(1, 21) if not s % x  } for x in range(2, 7)]
    print new_sets

if __name__ == "__main__":
    main()
