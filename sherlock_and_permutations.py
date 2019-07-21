#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, m):
    m = m - 1

    total = n + m

    return ((factorial(total)) // (factorial(m)*factorial(n))) %(10**9 +7)

def factorial(n):
    fact = 1
    for x in range(1, n):
        fact *= (x+1)
    return fact

if __name__ == '__main__':
    results = []

    t = int(input())

    for t_itr in range(t):
        nm = str(input()).split(" ")
        nm = [x for x in nm]

        n = int(nm[0])
        m = int(nm[1])

        result = solve(n, m)

        results.append(result)

    print(results)