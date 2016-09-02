#!/usr/bin/env python

import sys

def ifStatement(n):
    if n > 90:
        print "here", n,
        print "A"
    elif n > 80:
        print "B"
    elif n > 70:
        print "here", n,
        print "C"
    elif n > 60:
        print "D"
    else:
        print "E"

def forStatement(n):
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print "One more practise", n, 
        print w, len(w)

    for num in range(2, 10):
        if num % 2 == 0:
            print "Found an even number", num
            continue
        print "Found a number", num

    for num in range(20, 10, -1):
        if num % 2 == 0:
            print "Found an even number", num
            continue
        print "Found a number", num

    for num in range(len(words)-1, -1, -1):
        print num, "reverse order: ind:", words[num]


# really special syntax : For Else
def forElse():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break
        else:
            # loop fell through without finding a factor
            print n, 'is a prime number'

#def initlog():
def initlog(*args):
    pass # Remember to implement this!
    print "passed?"

def morePass():
    while True:
        # Busy-wait for keyboard interrupt (Ctrl+C)
        pass


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

def cube(x):
    return x**3

def oddOnly(x):
    return x % 2 == 0

def add(x, y):
    return x + y

if __name__ == "__main__":
    print sys.argv[1]
    num = int(sys.argv[1])
    ifStatement(sys.argv[1])
    ifStatement(num)

    forStatement(num)
    print forElse()

    initlog()
    #morePass()

    # The most useful form is to specify a default value for one 
    # or more arguments. This creates a function that can be called 
    # with fewer arguments than it is defined to allow.
    ask_ok('Do you really want to quit?')
    ask_ok('OK to overwrite the file?', 2)
    ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

    cubeVal = map(cube, range(1, 6))
    print cubeVal

    oddVal = filter(oddOnly, cubeVal)
    print oddVal

    sumVal = map(add, cubeVal, cubeVal)
    print sumVal

    
