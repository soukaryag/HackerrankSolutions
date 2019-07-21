#!/bin/python3

import os
import sys

#
# Complete the connectingTowns function below.
#
def connectingTowns(n, routes):
    product = 1
    for r in routes:
        product *= r

    return product % 1234567

if __name__ == '__main__':
    results = []
    t = int(input())

    for t_itr in range(t):
        n = int(raw_input())

        routes = list(map(int, raw_input().rstrip().split()))

        result = connectingTowns(n, routes)

        results.append(result)

    print(results)
