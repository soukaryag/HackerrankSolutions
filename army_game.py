#!/bin/python3

import os
import sys

#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    # swtich, make n the smallest always
    if n > m:
        temp = m
        m = n
        n = temp

    # base case
    if n <= 2:
        if m%2 == 0:
            return int(m/2)
        else:
            return int(m//2 + 1)

    # recursive case
    if m%2 == 0:
        hold = m/2
    else:
        hold = m//2 + 1

    return int(gameWithCells(n-2, m)) + int(hold)

    

if __name__ == '__main__':
    nm = str(raw_input()).split(' ')

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    print(result)
