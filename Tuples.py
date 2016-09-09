#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
list[2] = 1000     # Valid syntax with list

# tuple[2] = 1000    # Invalid syntax with tuple


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup4 = (50,)

print tup3

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

# ok to re-assign
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3

# del tup3[1]
# TypeError: 'tuple' object doesn't support item deletion

del tup3;
print "After deleting tup : "
# print tup3
# NameError: name 'tup3' is not defined
