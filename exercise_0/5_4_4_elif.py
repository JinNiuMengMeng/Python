#!/usr/bin/python
while(1):
    num = raw_input('Enter a number: ')
    print type(num)
    if (num == 'q'):
        break
    else:
        num = int(num)
        print type(num)
        if num > 0:
            print 'The number is positive'
        elif num < 0:
            print 'The number is negative'
        else:
            print 'The number is zero'
