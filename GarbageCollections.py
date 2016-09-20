#!/usr/bin/python


import gc
#print "Garbage collection thresholds:%r"%gc.get_threshold()

print gc.get_threshold()

def make_cycle():
    l = [1, 2]
    l.append(l)
    print l
    print len(l)

    print l[2]
    print len(l[2])

    print l[2][2]
    print len(l[2][2])    

make_cycle()

print gc.collect()

