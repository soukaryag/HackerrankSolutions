#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    primes = get_primes()
    product = 1
    total = 0
    while product <= n:
        product *= primes[total]
        total += 1

    return total - 1   
    
def get_primes():
    primes = []
    for x in range(2, 80):
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
                break 
        if prime:
            primes.append(x)

    return primes

if __name__ == '__main__':
    q = int(input())

    results = []

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)
        results.append(result)

    print(results)