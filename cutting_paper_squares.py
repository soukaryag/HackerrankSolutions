#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m):
    return (n*m)-1


if __name__ == '__main__':
    nm = raw_input().split(' ')

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    print(result)
