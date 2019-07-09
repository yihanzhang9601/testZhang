#!/usr/bin/env python37
# -*- coding : UTF-8 -*-
# 文本文件相关信息统计
# sys.argv[1:] 就是提取传入的参数1后面的变量
import sys  # 导入sys模块（内含很多函数方法和变量）
import os   # 导入os模块（包含普遍的操作系统功能）
def parse_file(path):
    """
    分析给定文本文件，返回其空格、制表符、行的相关信息
    :arg path: 要分析的文本文件的路径
    :return: 包含空格数、制表符数、行数的元组
    """
    wenjian = open(path)   # 打开文件
    i = 0                       # 空格
    spaces = 0                  # 制表符
    tabs = 0                    # 行数
    # enumerate：在序列中循环时，索引位置和对应值可以使用它同时得到
    for i,aa in  enumerate(wenjian):
        spaces += aa.count('')
        tabs += aa.count('\t')
    wenjian.close()         # 关闭文件
    # 以元组结构返回结果
    return spaces,tabs,i+1
def main(path):
    """
    函数用于打印文件分析结果
    :arg path:要分析的文本文件的路径
    :return:若文件存在则为 True，否则 False
    """
    if os.path.exists(path):
        spaces,tabs,lines = parse_file(path)
        print("spaces {}.tabs {}. lines {}".format(spaces,tabs,lines))
        return True
    else:
        return False
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

print()