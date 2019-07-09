#!/usr/bin/env python37
# -*- coding : UTF-8 -*-
# 文件处理
# open() 打开文件   参数：读：r、写：w、追加：a、
# file object = open(file_name[,access_mode][,buffering])
file = open("test.txt","w" )
print("文件名：",file.name)
print("是否已经关闭：",file.closed)
print("访问模式：",file.mode)
file.close()    # 关闭打开的文件

# write() \n:换行
fo = open('foo.txt','w')    # 打开文件
# 写入文件
fo.write("""               
def daxie(x)
    return [i.title() i in range()]
def gaoj(c,x)
    return c(x)      
         """)
print("down")
fo.close()                   # 关闭文件
# read()
# 打开文件
fo1 = open('foo.txt','r')
# 读取文件前()行
str = fo1.read()
print("读取的内容为:",str)
# 遍历循环读取文件每一行
fo2 = open('foo.txt')
for i in fo2:
    print(i,end="")
fo2.close()
# 拷贝文件