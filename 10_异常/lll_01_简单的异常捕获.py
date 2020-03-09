try:
    num = int(input("请输入一个整数"))
except:
    print("请输入正确的整数")
print("-" * 50)

"""
异常
符合语法规则也有可能报错，你不知道用户会输入什么鬼东西
Python解释器抛出异常后要针对性处理，从而保证程序的稳定性和健壮性

捕获异常

try:
    尝试执行的代码
except:
    出现错误的处理
"""
