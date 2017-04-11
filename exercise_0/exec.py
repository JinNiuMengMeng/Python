#!/usr/bin/python
fibs = [0, 1]
while 1:
    num = int(raw_input('please input a number:' ))
    if num == 0:
        break
    for i in range(num):
        fibs.append(fibs[-2] + fibs[-1])
    print fibs
