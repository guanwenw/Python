#!/usr/bin/python


def createGenerator() :
    # 0,1,2
    mylist = range(3)
    for i in mylist :
        yield i*i


def test():
    
    x = ['ab', 'cd']
    for i in x:
        # x.append(i.upper()) 
        # x will be updated in for loop
        # and cause dead loop
        print(x)
    
    
    x = 'abcd'
    for i in range(len(x)):
        x = 'a'
        print(x)
    print(x)


if __name__ == "__main__":

    mygenerator = createGenerator() # create a generator
    print(mygenerator) # mygenerator is an object!
    #<generator object createGenerator at 0xb7555c34>
    for i in mygenerator:
        print(i)

    test()

