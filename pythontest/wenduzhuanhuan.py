#/usr/bin/env python37
# -*- coding:UTF-8 -*-
fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 转换为摄氏度
    print("{:5d} {:7.2f}".format(fahrenheit , celsius))
    #{:5d} 的意思是替换为 5 个字符宽度的整数，宽度不足则使用空格填充
    #其中7指宽度为7，.2f指保留两位小数。
    fahrenheit = fahrenheit + 25