#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print str(tinydict)
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

if 2 in dict:
   print "2 is available in the given dict"
else:
   print "2 is not available in the given dict"


# does not work for value in dict
val = 'john'
if val in tinydict:
   print val + " is available in the given dict"
else:
   print val + " is not available in the given dict"

key = 'code'
if key in tinydict:
   print key + " is available in the given dict"
else:
   print key + " is not available in the given dict"


for k in tinydict:
    print k
    print tinydict[k]

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

dict['Age'] = 'String'
print "dict['Age']: ", dict['Age']

del dict['Name']; # remove entry with key 'Name'
# print "dict['Name']: ", dict['Name']
# KeyError: 'Name'

dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

# print "dict['Age']: ", dict['Age']
# print "dict['School']: ", dict['School']
# TypeError: 'type' object has no attribute '__getitem__'
