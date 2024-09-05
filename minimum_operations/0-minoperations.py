#!/usr/bin/python3
"""
finding minimum number of operations on copy and paste
"""


def minOperations(n):
    """
    fewest number of operations that result to n and H in the file.
    """

    if n <= 1:
        return 0

    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i
    return n
