#!/usr/bin/python

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

if 786 in list:
    print "786 in list"

for l in list:
    print l


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

print list1
del list1[2];
print "After deleting value at index 2 : "
print list1

print len([1, 2, 3])
print [1, 2, 3] + [4, 5, 6]
print ['Hi!'] * 4
print 3 in [1, 2, 3]

for x in [1, 2, 3]: print x,

print max(list1)
print max(list2)

list2.append(2)
list2.append(2)
list2.append(3)

print list2.count(2)
print list2.count(3)

print list2.sort()
print list2

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ]
print sorted(student_tuples, key=lambda student: student[2])   # sort by age
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print sorted(student_tuples, key=lambda student: student[2], reverse=True)   # sort by age

def numeric_compare(x, y):
    return x - y

def customize(x, y):
    return y - x 

print sorted([5, 2, 4, 1, 3], cmp=numeric_compare)
print sorted([5, 2, 4, 1, 3], cmp=customize)
