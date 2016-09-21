import sys, gc
 
def make_cycle(i):
    l = { }
    l[0] = l
    
    print '----- Printing  ', i, '-----'
    print l
    print len(l)

    print l[0]
    print len(l[0])
 
def main():
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)
    print "Creating cycles..."
    for i in range(10):
        make_cycle(i)
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)
 
if __name__ == "__main__":
    ret = main()
    sys.exit(ret)

