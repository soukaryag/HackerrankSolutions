#!/bin/python3

import os
import sys

#
# Complete the lights function below.
#
def lights(n):
    return ((2**n) - 1) % (10**5)

if __name__ == '__main__':
    results = []
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        results.append(result)

    print(results)