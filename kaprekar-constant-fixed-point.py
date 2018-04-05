# Get the fixed point of all 4 digit numbers i.e. how many iterations it 
# takes for the number to converge to the kaprekar constant
# https://en.wikipedia.org/wiki/6174_(number)

import sys

KAPREKAR_CONSTANT = 6174

def max_and_min(num):

    d1 = int(num/1000)
    d2 = int(num/100) - d1*10
    d3 = int(num/10) - d1*100 - d2*10
    d4 = num - d1*1000 - d2*100 - d3*10

    lst = [d1, d2, d3, d4]
    lst.sort()
    minnum = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]

    lst.reverse()
    maxnum = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]

    return (maxnum, minnum)

def reduce(num):

    (num1, num2) = max_and_min(num)

    #print (str(num1) + ' ' + str(num2))

    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def reduce_to_kaprekar_constant(num):
    count = 0
    while num != KAPREKAR_CONSTANT:
        count += 1
        num = reduce(num)
        if num == 0:
            break

    return count

def main():

    fixed_point_map = {}

    for i in range(1000, 10000):

        num_steps = reduce_to_kaprekar_constant(i)
        fixed_point_map[i] = num_steps

        print (str(i) + ' ' + str(num_steps))

if __name__ == '__main__':
    main()
