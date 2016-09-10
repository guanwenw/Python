#!/usr/bin/python

# Import module support
import support

# Now you can call defined function that module as follows
support.print_func("Zara")


# Namespaces and scoping
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print Money
AddMoney()
print Money


# Import built-in module math
import math
# The dir() built-in function returns a sorted list of strings
# containing the names defined by a module.
content = dir(math)
print content
