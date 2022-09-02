# A abundant number is one that is a sum of all its factors
# is greater than the number itself
# For example:
#   12 has factors 1, 2, 3, 4, 6
#   1 + 2 + 3 + 4 + 6 = 16 > 12
# Find all abundant numbers below the specified limit

import sys
import functools
from numbertheory import *

def main(limit):

    for i in range(2, limit):
        factors = factorize(i)

        sum_of_factors = functools.reduce((lambda x, y: x+y), factors)

        if sum_of_factors > i:
            print (int(i))

if __name__ == '__main__':
    main(int(sys.argv[1]))
