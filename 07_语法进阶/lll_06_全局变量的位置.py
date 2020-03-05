"""
全局变量定义的位置：在开发时，应该吧模块中的所有全局变量
定义在所有函数上方，就可以保证所有函数都能够正常的访问到每一个全局变量了
"""

"""
代码结构应该是
    shebang
    import模块
    全局变量
    函数定义
    执行代码
"""
# 错误示范
# num = 10
#
#
# def demo():
#     print(num)
#     print(title)
#     print(name)
#
#
# title = "lll"
#
# demo()
#
# name = "xiaoming"

num = 10
name = "xiaoming"
title = "lll"


def demo():
    print(num)
    print(title)
    print(name)


demo()
