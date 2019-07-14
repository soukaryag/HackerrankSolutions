#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):
    horizontalDistance = qx - px
    verticalDistance = qy - py

    return qx+horizontalDistance, qy+verticalDistance


if __name__ == '__main__':
    n = int(input())

    results = []

    for n_itr in range(n):
        pxPyQxQy = str(raw_input())
        pxPyQxQy = [x for x in pxPyQxQy]

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)
        results.append(result)

    print(results)
