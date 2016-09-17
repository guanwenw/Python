#!/usr/bin/python

class JustCounter:
    # private
    __secretCount = 0
  
    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

print counter._JustCounter__secretCount

# AttributeError: JustCounter instance has no attribute '__secretCount'
print counter.__secretCount
