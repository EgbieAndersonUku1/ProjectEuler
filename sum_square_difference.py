# -*- coding: utf-8 -*-

'''
project 6

he sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
'''


def difference_of_squares(number):
    """difference_of_squares(int) -> return(int)
    number : int
    return : int

    Takes a number and returns the difference of the square of the number
    """
    sum_of_square = 0
    square_of_sum = 0

    for i in xrange(1, number+1):

        sum_of_square += i**2 # take the sum of the square of the number
        square_of_sum += i    # the sum square of the natural numbers

    return abs(sum_of_square - square_of_sum**2) # return the difference


print(difference_of_squares(100))
