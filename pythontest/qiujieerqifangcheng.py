#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#求解二次方程
import math
a = int(input("Enter value of a："))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
d = b * b - 4 * a * c
if d < 0:
    print("roots are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1 = ", root1)
    print("Root 2 = ", root2)