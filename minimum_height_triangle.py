#!/bin/python3

import sys

def lowestTriangle(base, area):
    # Complete this function
    height = (2*float(area))/float(base)
    return int(round(height+.5))


base = int(input())
area = int(input())
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)