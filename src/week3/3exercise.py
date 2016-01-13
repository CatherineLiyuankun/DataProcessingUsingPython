# This Python file uses the following encoding: utf-8

# 有5名某界大佬xiaoyun、xiaohong、xiaoteng、xiaoyi和xiaoyang，其QQ号分别是88888、5555555、11111、12341234和1212121，用字典将这些数据组织起来。编程实现以下两个功能：
#
# （1）用户输入某一个大佬的姓名后可以输出其QQ号；
#
# （2）寻找所有有QQ靓号（5位数或小于5位数）的大佬，输出所有姓名（请将结果写在一行，中间用一个空格分隔）。

dict1 = {'xiaoyun': 88888, 'xiaohong': 5555555, 'xiaoteng': 11111, 'xiaoyi': 12341234, 'xiaoyang': 1212121}
name = raw_input("Please input the name:")
print dict1[name]
listV = dict1.values()
listK = dict1.keys()
print "Who has the nice QQ number?"
for i in range(0, len(listV)):
    if listV[i] < 100000:
        print listK[i]
