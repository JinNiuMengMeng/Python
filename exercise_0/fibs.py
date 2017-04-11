#!/usr/bin/python
def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result
num = int(raw_input('Num:'))
while num > 0:
    print fibs(num)
    num = int(raw_input('Num:'))
