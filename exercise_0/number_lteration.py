#!/usr/bin/python

strings = ['abc', 'def', 'uvw', 'xyz', 'abc', 'def']
#for string in strings:
#    if 'abc' in string:
#        index = strings.index(string)
#        print index
for index, string in enumerate(strings):
    if 'abc' in string:
        strings[index] = '[cenxored]'
        print index
