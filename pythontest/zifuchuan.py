#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
# 字符串换行
a = ("""
 Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
""")
print(a)
b = (
     "1" 
     "1"
     "1"
)
print(b)
b = b.split(" " ,3) # split() 以空格分隔，分三次
print(b)
z = 'da xia xie'
z1 = z.upper()      # 大写
print(z1)
z2 = z.lower()      # 小写
print(z2)
z3 = z.title()      # 首字母大写
print(z3)

# 文本搜索
s = "faulty for a reason"
s.find("for")   # 有的话返回 首个字符位置，没有找到则返回 -1

# 回文检查
s = input('Please enter a String:')
s1 = s[:: -1] # 把输入的字符串s，进行倒序处理形成新的字符串 s1
if s == s1:
    print('The string is a palindrome')
else:
    print("The string is not a palindrome")

# 格式化操作符
# %s、%d、格式符为真实值预留位置，并控制显示的格式
print("my name is %s.I am %d years old" % ('Shixiaolou',4)) # 链接参数时 + %
# 单词计数
v = input("输入一行：")
print("这一行数字为 %s " % (len(v.split(' '))))