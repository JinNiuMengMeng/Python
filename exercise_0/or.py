#!/usr/bin/python
while(1):
    number = int(raw_input('Enter a number greater 1 or 10:'))
    if number >= 10 or number >= 1:
        print 'This number is greater 1 or 10'
    else:
        print 'This number is greater less than 0'
