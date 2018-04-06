# A perfect number is one that is a sum of all its factors
# For example:
#   6 = 1 + 2 + 3
#   28 = 1 + 2 + 4 + 7 + 14
# Find all perfect numbers below the specified limit

import sys
import functools

def factorize(num):
    factors = []

    for i in range(1, int(num/2)+1):
        if num % i == 0:
            factors += [i]

    return factors

def main(limit):

    for i in range(2, limit):
        factors = factorize(i)
        #print (str(i) + ' --> ' + str(factors))
        
        sum_of_factors = functools.reduce((lambda x, y: x+y), factors)

        if sum_of_factors == i:
            print (int(i))

if __name__ == '__main__':
    main(int(sys.argv[1]))
