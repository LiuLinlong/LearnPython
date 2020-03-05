"""
函数内部修改全局变量的值——global
"""
number = 10


def demo3():
    # 希望修改全局变量的值
    # 使用global声明一下变量即可
    # global关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时就不会创建局部变量
    global number
    number = 99
    print("demo3 ==> %d" % number)


def demo4():
    print("demo4 ==> %d" % number)


demo3()
demo4()
