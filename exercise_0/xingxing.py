#!/usr/bin/python
def with_start(**params):
    print params['name'], 'is', params['age'], 'years old'
def without_start(params):
    print params['name'], 'is', params['age'], 'years old'
args = {'name':'Mike', 'age':42}
with_start(**args)
without_start(args)
 
