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
    """
    Check if a number that is a power of two
    """
    log = math.log(n, 2)
    power = math.pow(2, round(log))

    if n == power:
        return True
    else:
        return False

def getAdditiveSequence(n, first, second):
    """
    Get the values of an integer sequence which is additive i.e.
    the next number is the sum of the previous two.
    eg - With seed 0 and 1, we have the Fibonnaci numbers
    and with seed 2 and 1, we have the Luacs numbers
    """
    lst = []
    curr = first
    nxt = second
    n = n - 2
    lst.append(curr)
    lst.append(nxt)

    while n >= 0:
        curr, nxt = nxt, curr+nxt
        lst.append(nxt)

        n = n - 1

    return lst

def getFibonnaci(n):
    """Returns a list of the first n fibonnaci numbers."""
    return getAdditiveSequence(n, 0, 1)


def getLucas(n):
    """Returns a list of the first n Lucas numbers."""
    return getAdditiveSequence(n, 2, 1)
