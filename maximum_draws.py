#!/bin/python3

import os
import sys

#
# Complete the maximumDraws function below.
#
def maximumDraws(n):
    if n == 1:
        return 2
    else:
        return n+1

if __name__ == '__main__':
    results = []
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = maximumDraws(n)
        results.append(result)

    print(results)