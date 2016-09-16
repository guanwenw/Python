#!/usr/bin/python

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   # Base class for all exceptions
   # then 
   # StopIteration, SystemExit, StandardError
   except Exception, Argument:
   #except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
temp_convert("xyz");


def functionName( level ):
   if level < 1:
      raise "Invalid level!", level
      # The code below to this would not be executed
      # if we raise the exception

functionName(0)
