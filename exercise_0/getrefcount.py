#!/usr/bin/python
import sys

print sys.getrefcount("abc")
a = "abc"
b = "abc"
c = "abc"
d = "abc"
print sys.getrefcount("abc")
a = 1
print sys.getrefcount("abc")
b = 2
print sys.getrefcount("abc")
