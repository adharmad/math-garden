# print differences between prime numbers between 1 and n
import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    diffMap = getPrimeDiff(n)

    for k in diffMap:
        print (str(k[0]) + "-" + str(k[1]) + " = " + str(diffMap[k]))
