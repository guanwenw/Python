#!/usr/bin/python
import string

var = 100
if var == 100: print "val is", var

str1 = "Hello World!"
if str1[0] == 'H': print str1[0]
if str1[0] == "H":
    print str1[0]

if str1[2:4] == "ll":
    print str1

if str1[2:3] != "ll":
    print str1[:3]
    print "Updated String :- ", str1[:6] + 'Python'


print "My name is %s and weight is %d kg!" % ('Zara', 21) 
    
print max(str1)
print min(str1)

print str1.upper()
print str1
