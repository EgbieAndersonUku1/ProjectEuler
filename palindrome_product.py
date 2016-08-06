
# -*- coding: utf-8 -*-

# problem 4
#A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import time

def is_pallindrome(number):
    """is_prime(int) -> return(boolean)

    number : int
    return : boolean -> return True if the number is a boolean and false otherwise
    Checks whether a given number is a prime number

    >>> is_prime(9009)
    True
    >>> is_prime(1234)
    False
    """
    new_num = str(number)
    return new_num == new_num[::-1] # reverse the number and check if its the same


def get_largest_pallindrome():
    """get_largest_pallindrome(None) -> return(int)

    Returns the largest palindrome from a three digit number
    """

    largest = 0
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            product = i*j
            if is_pallindrome(product) and product > largest:
                largest = product
    return largest


print(get_largest_pallindrome())
