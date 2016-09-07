#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
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

# iterate dict
for k in tinydict:
    print k
    print tinydict[k]
