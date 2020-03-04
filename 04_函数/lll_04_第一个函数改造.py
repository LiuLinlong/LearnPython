name = "小明"


# Python解释器指导下方定义了一个函数


def say_hello():
    """打招呼三次"""

    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)
# 只有在程序中主动调用函数，才会让函数执行
say_hello()
print(name)

# 这个程序的意义在于让自己明白带函数的代码的执行顺序
# 函数调用必须在函数定义的下方，必须保证Python解释器以及知道函数的存在
"""
调试的时候step over与step into的区别：into会进入自定义函数内部逐步执行
"""

"""
函数的文档注释：
在函数的第一行使用多行注释
"""
