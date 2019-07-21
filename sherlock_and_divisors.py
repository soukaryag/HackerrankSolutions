#!/bin/python3

import os
import sys

#
#
# Complete the divisors function below.
#
def divisors(n):
    count = 0
    for x in range(1, int(n**0.5)+1):
        hardDiv = n//x
        if n % x == 0 and x != hardDiv and x % 2 == 0:
            count += 1
        if n % (hardDiv) == 0 and (hardDiv) % 2 == 0:
            count += 1

    return count
    

if __name__ == '__main__':
    results = []

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)
        results.append(result)

    print(results)