"""
字符串包含很多方法（ipython下创建1个字符串，输入.然后Tab）
    1.判断类型的方法有九个 都是is开头
    2.查找和替换有七个
    3.大小写替换有五个
    4.文本对齐有三个
    5.去除空白字符有三个
    6.拆分和连接有五个
"""

"""
代码中只有每一类常用或者易混的
"""
# \n和\r区别
# unix下\n是换行，Windows下是先\r回车到行尾再\n换行

# isspace()可以判断空白字符
space_str = "   "
print(space_str.isspace())
space_str = "\t\n\r\n"
print(space_str.isspace())

# 是否只包含数字
# 区别：
# 1.都不能判断小数
# 2.unicode字符串 \u转义 后两个可以
# 3.isnumeric可以判断中文数字
num_str = "\u00b2"  # 平方符号
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
