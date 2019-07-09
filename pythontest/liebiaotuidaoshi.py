#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#列表推导式
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# 列表推导式写法
squares2 = [x**2 for x in range(9)]
print(squares2)

comds = []
for i in [1,2,3]:
    for j in [3,1,4]:
        if i != j:
            comds.append((i,j))
print(comds)

# 列表推导式写法
a = [(i,j)for i in [1,2,3] for j in [3,1,4] if i != j]
print(a)

a = [1,2,3]
z = [x + 1 for x in [x**2 for x in a]]
print(z)