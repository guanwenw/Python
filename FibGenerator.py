#!/usr/bin/python

def fib(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        print b 
        a, b = b, a + b 
        n = n + 1

fib(5)

# -----------------

def fibList(max): 
    n, a, b = 0, 0, 1 
    L = [] 
    while n < max: 
        L.append(b) 
        a, b = b, a + b 
        n = n + 1 
    return L

print fibList(5)
for i in fibList(5):
    print i

# -----------------

for i in range(1000): pass
for i in xrange(1000): pass

# -----------------

class Fib(object): 

    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()

for f in Fib(5):
    print f

# -----------------

def fibYield(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

for f in fibYield(5):
    print f

# -----------------

f = fibYield(5)
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
# StopIteration
# print f.next()

# -----------------

from inspect import isgeneratorfunction 
print isgeneratorfunction(fibYield) 
# True

# -----------------

import types 
print isinstance(fibYield, types.GeneratorType) 
# False 
print isinstance(fibYield(5), types.GeneratorType) 
# True

# -----------------

f1 = fibYield(4)
f2 = fibYield(3)
print 'f1: ', f1.next()
print 'f2: ', f2.next()
print 'f2: ', f2.next()
print 'f2: ', f2.next()
print 'f1: ', f1.next()
print 'f1: ', f1.next()
print 'f1: ', f1.next()
