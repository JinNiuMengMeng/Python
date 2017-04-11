#!/usr/bin/python

d = {'x':1, 'y':2, 'z':3}
for key, value in d.items():
    print key, 'corresponds to', value

for key in d:
    print key, ':', d[key]
