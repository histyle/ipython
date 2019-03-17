
#str()： 函数返回一个用户易读的表达形式。
#repr()： 产生一个解释器易读的表达形式。
#rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。如 ljust() 和 center(), zfill(), 它会在数字的左边填充0
for x in range(1,10):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))


for x in range(1,10):
    print('{0:3d} {1:4d} {2:5d}'.format(x,x*x,x*x*x))


print('{0} and {1}'.format('google','runoob'))
print('{1} and {0}'.format('google','runoob'))   


print('{name}网址：{site}'.format(name="菜鸟教程",site="www.runoob.com"))

print("站点列表：{0},{1},{other}".format("google","baidu",other="runoob"))


###########
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}

for name, num in table.items():
    print('{0:10} ==> {1:10d}'.format(name,num))

print('Runoob:{0[Runoob]:5d}, Google:{0[Google]:5d},Taobao :{0[Taobao]:5d}'.format(table))

str_input = input("input: ")
print("your input is {}".format(str_input))