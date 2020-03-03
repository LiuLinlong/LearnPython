"""
循环计算开发步骤
1.编写循环 确认要计算的数字
2.添加结果变量，在循环内部处理计算结果
"""

i = 0
res = 0
while i <= 100:
    if i % 2 == 0:
        res += i  # 缩进的位置很重要
        # print(i)
    i += 1
print("100内的偶数和为 %d" % res)

"""
break和continue
break   某一条件满足时，退出循环，不再执行后续重复的代码
continue    某一条件满足时，不执行后续重复代码

break和continue只对当前所在循环有效
"""
