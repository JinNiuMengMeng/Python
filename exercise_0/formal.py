#!/usr/bin/python
width = input('please enter width:')

price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width
print header_format % (item_width, 'Item', price_width, 'price')
print '-' * width
print format % (item_width, 'Apples', price_width, 4)
print format % (item_width, 'Pears', price_width, 0.6)
print format % (item_width, 'Cantaloupes', price_width, 6.0)
print format % (item_width, 'Dried Apricots (16 oz.)', price_width, 6.0)
print format % (item_width, 'Priunes (4 lbs.)', price_width, 45)
print '=' * width

