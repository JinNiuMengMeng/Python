#!/usr/bin/python
while(1):
    number = int(raw_input('Enter a number between 1 and 10:'))
    if number <= 10 and number >= 0:
        print 'This number is greater than 0 and less than 10'
    else:
        print 'This number is greater than 10'
