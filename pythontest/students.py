#/usr/bin/env python37
# -*- coding : UTF-8 -*-
# 判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生物理、数学、
# 历史三科的成绩，如果总成绩小于 180，程序打印 “failed”，否则打印 “passed”。
n = int(input("学生数量为："))
date = {} #定义字典存储数据
date2 = {}
kemu = ['物理','数学','历史'] # 列表定义科目
for i in range(0,n):
    name = input('学生姓名为：'.format(i))    # 学生名称
    marks = []  # 定义列表存储学生分数
    for j in kemu:
        marks.append(float(input('{}分数为: '.format(j))))  # 向列表添加科目分数
        date[name] = marks  # 将姓名，分数存入字典
        print(date)
for i,j in date.items(): # 遍历字典
    total = sum(j)       # 求学生分数和
    print('学生',i,'分数和为:',total)
    if total <= 180:
        print(i,':failed')
    else:
        print(i,':passed')