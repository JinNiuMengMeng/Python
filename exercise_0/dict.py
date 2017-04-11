#!/usr/bin/python

a = "this is %(whose)s %(fruit)s !" % {'whose':'my', 'fruit':'apple'}
print a

b = "this is %s %s" % ('my', 'apple')
print b

c = "This is {} {}" .format('my', 'apple')
print c

d = "this is {1} {0}" .format('apple', 'my')
print d

e = "this is {whose} {fruit}" .format(fruit = 'apple', whose = 'my')
print e
