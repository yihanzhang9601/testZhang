#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
# 数据结构
#列表
a = [23,45,66,22,99,4,67]
a.append(77) # 添加元素 77 到列表末尾
print(a)
a.insert(2,33) # 添加元素 33 到指定位置
print(a)
print(a.count(23)) # 检查列表中 23 出现了几次
a.remove(23) # 删除列表中的指定数值 23
print(a)
del a[1] # 删除指定位置的列表元素
print(a)
a.reverse() # 翻转整个列表
print(a)
b = [69,71,96]
a.extend(b) # 将一个列表的所有元素添加到另一个列表的末尾
print(a)
a.sort() # 给列表排序
print(a)

#将列表用作栈和队列
a = [23,1,33,43,21,545,78,565,90,7]
a.pop() # 弹出列表的最后一个元素
print(a)
a.pop(0) # 弹出列表的第一个元素
print(a)