# print first n Lucas numbers
import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    lst = getLucas(n)

    for p in lst:
        print (p)
