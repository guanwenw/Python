#!/usr/bin/python

assert 1 in [1, 2, 3]      # lists
assert 4 not in [1, 2, 3]

s = {1, 2, 3}
assert 1 in s      # sets
assert 4 not in s
s.add(4)
assert 4 in s


assert 1 in (1, 2, 3)      # tuples
assert 4 not in (1, 2, 3)

d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
assert 4 not in d
assert 'foo' not in d  # 'foo' is not a _key_ in the dict

s = 'foobar'
assert 'b' in s
assert 'x' not in s
assert 'foo' in s  # a string "contains" all its substrings

x = [1, 2]
y = iter(x)
z = iter(x)

print type(x)
print type(y)

print next(y)
print next(y)

print next(z)
print next(z)
print next(y)

