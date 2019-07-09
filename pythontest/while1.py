#！usr/bin/env python37
#-*- coding:UTF-8 -*-
#计算投资

# w = 20
# while w >=1:
#     print(w)
#     w -=1           # w = w - 1

amout = float(input("输入金额:"))
inrate = float(input("输入利率:"))
period = int(input("输入期限:"))
value = 0
year = 1
while year <= period:
    value = amout + (inrate * period)

    #Year{}Rs.{:.2f}".format(year, value) 称为字符串格式化，大括号和其中的字符会被替换成传入
    # str.format() 的参数，" \"也即 year 和 value。其中 {:.2f} 的意思是替换为 2 位精度的浮点数。
    print("Year {} Rs. {:.2f}".format(year,value))
    amout = value
    year = year + 1