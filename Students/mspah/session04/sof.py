#!/usr/bin/env python


def main(n):
    # Let's create a binary array, and a blank array for the primes found
    binary_array, primes = [True] * (n+1), []

    for p in xrange(2, n+1):
        # if b[p] is true, we append to ps
        # because p is 2, and prime we apply it
        if binary_array[p]:
            primes.append(p)

            """
            our second loop, this will start at the value of p
            and go up to our max, in increments of p
            so we know all these numbers are not prime, because they are divisible by p, so we change their value to False.
            first this will remove all the numbers divisible by 2, then 3, 5, and then 7.
            if it runs into a false bit in the binary array, it won't hit the second loop
			"""
            for i in xrange(p, n+1, p):
                binary_array[i] = False
    print primes

if __name__ == "__main__":
    main(500)