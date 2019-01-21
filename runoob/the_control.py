#!/usr/bin/env python

a, b = 0, 1

while b < 10:
    print(b)
    a, b = b, a + b


###
var = 100
if var:
    print("is ture")
    print(var)



age = int(input("please your dog's age: "))
print("")

if age < 0:
    print("你现在开玩笑么")
elif age ==1:
    print("equal human 14 age")
elif age ==2:
    print("equal human 22 age")
elif age > 2:
    human = 22 + (age -2)*5
    print("equal human ", human ," age")

#input("点击 enter 键退出")
