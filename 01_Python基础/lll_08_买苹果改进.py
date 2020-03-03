# 1.输入苹果单价
price = float(input("请输入苹果的单价："))
# 2.输入苹果重量
weight = float(input("请输入苹果的重量："))
# 3.计算支付总金额
money = price * weight

print(money)
"""
输入：用代码获取键盘输入的信息
input函数
字符串 = input("提示信息")
注意：是字符串

类型转换函数
    int()
    float()

字符串
    拼接：使用 +
    重复多次： 使用 * 
字符串和数值变量不能进行其他运算 
"""