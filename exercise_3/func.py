#!usr/bin/python
#codding:utf-8
def add(num1, num2, *num):
    if isinstance(num1, int) and isinstance(num2, int):
        print num1 + num2
    else:
        print 'error'
    d = 0
    for i in num:
        d += i
    return d
print add('a', 2, 3, 3)
