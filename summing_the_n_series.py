#!/bin/python3

import os
import sys

#
# Complete the summingSeries function below.
#
def summingSeries(n):
    return (n*n) % 1000000007


if __name__ == '__main__':
    results = []

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        results.append(result)

    print(results)
