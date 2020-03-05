"""
要求：
有两个整数变量 a = 6, b = 100
不使用其他变量，交换两个变量的值
"""
a = 6
b = 100
# 一般的解题思路
# 解法1. 使用临时变量
c = a
a = b
b = c
print(a)
print(b)
print(c)

# 解法2. 不使用其他变量
a = 6
b = 100
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# 解法3. Python专有
a = 6
b = 100
# a, b = (b, a)
# 提示：等号右边是一个元组，只是把小括号省略了
a, b = b, a
print(a)
print(b)
