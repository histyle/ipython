#!/usr/bin/env python

list = [1,2,3,4]

it = iter(list)
#print(next(it))

for i in it:
    print(i, end=" ")

print("")
import sys
s_list = ['a','b','c','d']

#print(s_list)
s_it = iter(s_list)
while True:
    try:
        print(next(s_it))
    except StopIteration:
        sys.exit()

