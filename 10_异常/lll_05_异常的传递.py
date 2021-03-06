def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)

"""
异常的传递   当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方
如果传递到主函数，仍然没有异常处理，程序才会被终止

Tips：
    在开发中，可以在主函数增加异常捕获
    而在主函数中调用其他的函数，只要出现异常，都会传递到主函数的异常捕获中
    这样就不需要在代码中，增加大量的异常捕获，能够保证代码的简洁
"""

"""
抛出raise异常
在开发中除了代码执行出错Python解释器会抛出异常外，还可以根据应用程序特有的业务需求主动抛出异常

示例：
提示用户输入密码，如果长度小于8，抛出异常

创建一个Exception类的对象
使用raise关键字抛出异常对象
"""