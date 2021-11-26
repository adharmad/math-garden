# print all primes between 1 and n
import sys, math

def getPrimes(n):
    """Returns a list of all primes between 2 and n."""
    lst = []
    lst.append(2)
    lst.append(3)

    for i in range(4, n):
        isnotprime = 0
        for p in lst:
            if i % p == 0:
                isnotprime = 1
                break
        if not isnotprime:
            lst.append(i)

    return lst

def getPrimePairs(n):
    """Returns a tuple of prime numbers separated by 2."""
    plst = getPrimes(n)

    pairLst = []

    for i in range(1, len(plst)):
        if plst[i] - plst[i-1] == 2:
            pairLst.append((plst[i-1], plst[i]))

    return pairLst

def getPrimeDiff(n):
    """Returns a map that represent difference between consecutive
    prime numbers.
    The key of the map is a tuple having the two prime numbers.
    The value of the map is the difference between them.
    """
    plst = getPrimes(n)

    diffMap = {}

    for i in range(1, len(plst)):
        diffMap[(plst[i], plst[i-1])] = plst[i] - plst[i-1]

    return diffMap

def isPowerOfTwo(n):
    log = math.log(n, 2)
    power = math.pow(2, round(log))

    if n == power:
        return True
    else:
        return False
