#!/usr/bin/python
sum = lambda arg1, arg2: arg1 + arg2;
while 1:
    a = int(raw_input("Plear input a value:"))
    b = int(raw_input("Plear input b value:"))
    if (a < 0) | (b < 0):
        break
    print sum(a, b)
