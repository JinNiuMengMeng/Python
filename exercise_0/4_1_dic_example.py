#!/usr/bin/python
people = {
        'Alice':{'phone':'2345', 'addr':'Foo drive 23'},
        'Beth':{'phone':'9734', 'addr':'Bar street 42'},
        'Cecil':{'phone':'3014', 'addr':'Baz avenue 50'}
        }

labels = {'phone':'phone number', 'addr':'address'}

name = raw_input('Name:')

request = raw_input('Phone number(p) or address(a)? Please input: ')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

if name in people:
    print "%s's %s is %s." %(name, labels[key], people[name][key])
#labels[key], 通过键的名字来查找相应的值.
