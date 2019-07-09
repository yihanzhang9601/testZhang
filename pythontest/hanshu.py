#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
# 函数
# 定义函数
def he(x,y):
    return x + y
# 调用函数
he1 = he(1,1)
print(he1)
# 函数：回文检查
def huiwenjiancha(s):
    return s == s[:: -1]
#if __name__=='__main__':   # 作为脚本时 执行下面代码；被调用时下面代码不执行
s = input('enter a string:')
if huiwenjiancha(s):
    print(1)
else:
    print(0)

# 局域变量
def cahngge():
    a = 90
    print(a)
a = 9
print(a)


# global 全局变量
b = 10
def changge():
    global b
    print(b)
    b = 100
print(b)
changge()
changge()  # 触发函数后 b 的值变为100
print(b)

# 默认参数值
def test(a, b= -99 ):
    if a > b:
        return True
    else:
        return False

test1 = test(12,17)
print(test1)

# 默认值参数可变写法
def test2(a,date=None):
    if date is None:
        date = []
        date.append(a)
        return date
test22 = test2(14)
test22 = test2(4)
print(test22)

# 关键字参数
def func(a = None,b=3,c=9):    # 以变量定义参数的默认值
    print('a = :',a,"b = :",b,"c = :",c)
func(3,6,9)
func(c = 1)

# 强制关键字参数
def hello(*,name='User'):
    print("hello",name)
hello1 = hello(name = "sdasd")

# 文档字符串
import math
def longest(a,b):
    """
     Function to find the length of the longest side of a right triangle.

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side c as float
    """
    return math.sqrt(a * a + b * b)
if __name__ == '__main__':
    print(longest.__doc__)
    print(longest(4,5))

# 高阶函数：函数作为参数
# 创建一个函数，将参数列表中的首字母变成大写
def high(l):
    return [i.title() for i in l]
if __name__ == '__main__':
    print("done")
# 创建一个高阶函数，接受一个函数和列表作为参数
def testg(h,l):
    return h(l)
cx = ['wesdc','wder','mnjs']
print(testg(high,cx))

# map :它接受一个函数和一个序列（迭代器）作为输入，
# 然后对序列（迭代器）的每一个值应用这个函数，
# 返回一个序列（迭代器），其包含应用函数后的结果
lst = [1,2,3,4,5]
def xiangc(num):
    return num * num
print(list(map(xiangc,lst)))

