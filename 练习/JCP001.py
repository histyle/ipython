#创建JCP001-100.py
'''
for x in range(2,101):
    if x < 10 :
        open("JCP00" + str(x) + ".py",mode="w")
    elif x < 100:
        open("JCP0" + str(x) + ".py",mode="w")
    else:
         open("JCP" + str(x) + ".py",mode="w")
'''
'''
【程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
　　　　　　掉不满足条件的排列。 
2.程序源代码：
'''

count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ( i != j ) and ( i != k ) and (j != k ):
                print(i*100 + j*10 + k)
                count += 1

print(count)