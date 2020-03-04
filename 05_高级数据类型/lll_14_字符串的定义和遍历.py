"""
一对单引号或双引号都可以定义字符串
但大多数语言都是双引号，所以优先选用双引号
"""
str1 = "Hello Python"
str2 = '我是一个"大西瓜"'

print(str1)
print(str2)

"""
字符串的索引是从0开始的
取值都是 [index]
"""
print(str1[6])

for char in str2:
    print(char, end="~")
