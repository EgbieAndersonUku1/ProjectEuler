"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143 ?

"""
import math
import ast

def load(f='primes.txt'):
    return open(f).read()

def sort_data():

    data = {}
    f = load()
    primes = f.split()

    for prime in primes:
        data[int(prime)] = True

    f = open('primes.txt', 'w')
    f.write(str(data))

primes = ast.literal_eval(load())
term = 600851475143
#term = 13195
biggest_prime = 0


for i in xrange(2, int(math.sqrt(term))):

    # check if the number is a prime and the number is divisable by the term
    if primes.get(i, False) and term % i == 0:
        if i > biggest_prime:
            biggest_prime = i

        # keep dividing the prime number as long as the remainder is 0
        while term % i == 0:
            term /= i # divide the prime number by i


print(biggest_prime)
