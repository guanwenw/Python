#!/usr/bin/python

from itertools import count
counter = count(start=13)

print next(counter)
print next(counter)


from itertools import cycle
colors = cycle(['red', 'white', 'blue'])

print next(colors), next(colors), next(colors), next(colors)


from itertools import islice
colors = cycle(['red', 'white', 'blue'])  # infinite
limited = islice(colors, 0, 4)            # finite
for x in limited:                         # so safe to use for-loop on
    print(x),

# build an iterator producing the Fibonacci numbers

class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1
 
    def __iter__(self):
        return self
 
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

    def next(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()
print list(islice(f, 0, 10))

print f.next()
print f.next()

it = iter(f)
print it.next()
