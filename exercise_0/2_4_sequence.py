#!/usr/bin/python
database = [
        ['albert', '1234'],
        ['dilbert', '4242'],
        ['smith', '7524'],
        ['jones', '9843']
        ]
username = raw_input('PIN code:')
pin = raw_input('PIN code:')
if[username, pin] in database: 
    print 'Access granted'
else:
    print 'Not access granted'