#!/usr/bin/python

n = [1,2,3]
print [x * x for x in n]

# note: this is not a tuple comprehension
m = (x * x for x in n)
print m.next()
print m.next()
print list(m)

print {x * x for x in n}

print {x : x * x for x in n}
