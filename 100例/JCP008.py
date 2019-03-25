'''
【程序8】
题目：输出9*9口诀。
1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
2.程序源代码：

'''


for x in range(1,10):
    for y in range(1,x + 1):
        print('%d * %d = % -4d' % (y,x,x*y), end = " ")
    print(" ")