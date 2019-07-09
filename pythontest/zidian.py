#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#字典 :字典是是无序的键值对集合（key:value）
date = {'一':'王敏','二':'李芳','三':'三时','四':'李峰','五':'金石','六':'赵丽'}
print(date)
print(date['一'])
date['六'] = '夜王'    # 添加新的键值对（变更原有键值对的值）
print(date)
del date['一']         # 删除指定键值对
print(date)

# in 关键字查询指定的键是否存在于字典中
print('一' in date)

dict((('1','11'),('2','22')))
print(dict((('1','11'),('2','22'))))
# items() 遍历一个字典
datt = {'一':'王敏','二':'李芳','三':'三时','四':'李峰','五':'金石','六':'赵丽'}
for x,y in datt.items():
    print(x,":"+y)

#  判断键值对是否存在，不存在创建一个默认值 dict.setdefault(key, default)
date2 = {'客户姓名':'秦朗','证件类型':'身份证','证件号码':'75237603293'}
date2.setdefault('性别', []).append('男')
print(date2)
date2.setdefault('性别', []).append('女')
print(date2)
# dict.get(key, default) 索引键，如果键不存在，那么返回指定的 default 值
print(date2.get('性别',0))
print(date2.get('性',0))
# enumerate() 遍历列表（或任何序列类型）的同时获得元素索引值
for i,j in enumerate(date2):
    print(i,j)
# zip() 遍历两个序列类型
a = ['name','age']
b= ['科盟','30']
for i,j in zip(a,b):
    print("{} : {}".format(i,j))