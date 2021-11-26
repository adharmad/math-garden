# print all mersenne primes between 1 and n
import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    lst = getPrimes(n)

    for p in lst:
        if isPowerOfTwo(p+1):
            print (p)
