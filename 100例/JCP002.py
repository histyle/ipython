'''
【程序2】
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成;
从键盘输入当月利润I，求应发放奖金总数？
1.程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　　　　　　
2.程序源代码：
'''


bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.500075
bonus4 = bonus2 + 200000 * 0.5
bonus6 = bonus4 + 200000 * 0.3
bonus10 = bonus6 + 400000 * 0.15

gain = int(input('input gain:'))
income = 0
if gain <= 100000:
    income = gain * 0.1
elif gain <= 200000:
    income = bonus1 + (gain - 100000) * 0.0075
elif gain <= 400000:
    income =  bonus2 + (gain - 200000) * 0.05
elif gain <= 600000: 
    income =  bonus4 + (gain - 400000) * 0.03
elif gain <= 1000000:
    income =  bonus6 + (gain - 600000) * 0.015
else:
    income =  bonus10 + (gain - 1000000) * 0.01


print("incame", income)    