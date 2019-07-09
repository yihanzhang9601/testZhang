#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#元组
#由数个逗号分隔的字符串组成
a = "wan","er","saw","wwf"
print(a)
print(a[0])
for i in a:
    print(i,end = '') # end = ""在循环中不换行

x,y = divmod(15,2) #divmod:返回一个包含商和余数的元组
print(x)
print(y)

i = 123,
print(type(i)) #type():查看变量的数据类型