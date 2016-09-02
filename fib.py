#!/usr/bin/env python

import os, fnmatch

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b


def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


# Jul 30, 2016
# Learn python, classical fib
def fib3(n): # return Fib series up to n
    result = []
    a, b = 0, 1
    while b < n:
        print b
        print 'The value of b is', b 
        print 'A trailing comma avoids the newline after the output', 
        a, b = b, a + b
    return b



if __name__ == "__main__":
    import sys
    num = int(sys.argv[1])
    fib(num)
    #print '\n';
    print fib2(num)
    fib(int(sys.argv[1]))
    print fib2(int(sys.argv[1]))
    print fib3(int(sys.argv[1]))

    
    name = '*.py'
    #name = '*.txt'
    pattern = '*nc'
    path = '/exa/validation/Thermal/' 
    #path = '/exa/validation/Thermal/' 
    print find('*nc', '/exa/validation/Thermal')
