"""
注意事项！：
    在函数内部，可以通过全局变量的引用获取对应的数据，但不能修改全局变量的引用
"""

number = 10


def demo3():
    # 希望修改全局变量的值
    # python中不能直接修改全局变量的引用
    # 如果使用赋值语句，会在函数内部定义一个局部变量（仅仅是和全局变量重名）
    number = 99
    print("demo3 ==> %d" % number)


def demo4():
    print("demo4 ==> %d" % number)


demo3()
demo4()
