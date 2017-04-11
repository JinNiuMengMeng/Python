#!/usr/bin/python
import sys
import string
fp = open('string.txt', 'w')
sys.stdout = fp
help(string)
fp.close()
