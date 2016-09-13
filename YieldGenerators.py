#!/usr/bin/python

import math

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append()

    return result_list

# Or a better way
def get_primes(input_list):
    return (element for element in input_list if is_prime(element))

# a way to check whether the number is prime
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


# Yield Generator
def get_primesIter(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_number_10():
    # Project Euler #10
    total = 2
    for next_prime in get_primesIter(3):
        if next_prime < 10:
            total += next_prime
        else:
            print(total)
            return

solve_number_10()

# TODO: Magic!

def get_primesMagic(number):
    print number
    while True:
        if is_prime(number):
            print 'before : ', number
            number = yield number
            print 'after : ', number
        number += 1

def print_successive_primes(iterations, base=10):
    prime_generator = get_primesMagic(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes(5)
