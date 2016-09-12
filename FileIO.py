#!/usr/bin/python

import os

# Open a file
fo = open("tryexcept.py", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

fo.write( "Python is a great language.\nYeah its great!!\n");


# Open a file
fo = open("tryexcept.py", "r+")

str = fo.read(10);
print "Read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position


# Close opend file
fo.close()

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

os.remove( "test2.txt" )
