# -*- coding: utf-8 -*-
"""
alias on EulerProject -

2520 is the smallest number that can be divided by each of the numbers from
 1 to 10 without any remainder.
 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
import time

def gcd(a, b):
    """gcd(int, int) -> return(int)
    a: integer
    b: integer
    return: integer

    Takes two numbers a, b and returns the gcd (greatest common divisor)
    of that number

    >>> gcd(90, 8)
    2
    >>> gcd(216, 594)
    """
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a

def lcm(a, b):
    """lcm(int, int) -> return(int)
    a: integer
    b: integer
    return: integer

    Takes two numbers a, b and returns the lcm (lowest common multiple)
    of that number

    >>> lcm(10, 9)
    90
    >>> lcm(9, 10)
    90
    """
    return (a/gcd(a, b)) * b

# time.clock()
# a, b = 1000000, 999999
# for i in xrange(999998, 1, -1):
#     a, b = lcm(a, b), i
# print a
# print(time.clock())
