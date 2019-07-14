#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    sum = 0
    for x in range(0, n):
        sum += x

    return sum

if __name__ == '__main__':
    results = []
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)
        results.append(result)

    print(results)