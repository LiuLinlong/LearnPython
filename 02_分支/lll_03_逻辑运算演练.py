"""
逻辑运算
逻辑运算符
    and/or/not
用逻辑运算符把多个条件逻辑连接

1.and
    条件1 and 条件2  #都成才成
2.or
    条件1 or 条件2  #都不才不
3.not
    not 条件
"""

# Exercise1
age = int(input("Please input your age:"))
# 判断要求人的年龄在0-120之间
"""
age = 10000
age >= 0 and age <= 120
age >= 0 or age <= 120
带入判断，用and
"""
if age >= 0 and age <= 120:
    print("correct")
else:
    print("wrong")
