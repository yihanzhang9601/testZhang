#!/usr/bin/env python37
# -*- coding:UTF-8 -*-
#计算工资
gongzi = 1500
ticheng = 200
choucheng = 0.02
danjia = int(input("物品单价为："))
shuliang = int(input("出售数量为："))
ticehnghe = ticheng * shuliang
shouchenghe = choucheng * danjia * shuliang
zsr = gongzi + ticehnghe + shouchenghe
print("提成和为 = {:6.2f}".format(shouchenghe))
print("总收入为：")
print(zsr)