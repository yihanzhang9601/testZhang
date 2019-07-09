#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#计算n个数字平均值
n = 5
sum = 0
count =0
print("请输入5个数字：")
while count < n:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / n
print ("n = {},sum = {}".format(n,sum))
print("average = {:.2f}".format(average))