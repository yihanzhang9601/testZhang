#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#集合
# 第一种方式创建集合
basket = {"apple","orange","apple","pear","orange","banana","agg"}
print(basket)   #重复的元素被去除
print("pear" in basket)
print("crabgrass" in basket)

# 第二种方式创建集合
# 演示对两个单词中的字母进行集合操作
a = set("skjd")
b = set("skjdcuisdcg")
# print(a)    # 去重后a集合的值
# print(b)
# print(a-b)  # a有而b没有的字母
# print(a&b)  # a和b都有的字母
# print(a^b)  # 存在于a或b但不同时存在的字母
print(a.pop())     # 随机删除一个元素
print(a)
a.add("c")  # 添加元素到集合
print(a)