# Find all pythagorean triplets below the upper bound specified

import sys, math

def is_pythagorean_triplet(a, b):
    c = int(math.sqrt(a*a + b*b))

    if c*c == a*a + b*b:
        return True
    else:
        return False

def main(limit):

    for a in range(1, limit+1):
        for b in range(a, limit+1):
            if is_pythagorean_triplet(a, b):
                c = int(math.sqrt(a*a + b*b))

                if c > limit:
                    continue

                print("{0}, {1}, {2}".format(a, b, c))

if __name__ == '__main__':
    main(int(sys.argv[1]))
