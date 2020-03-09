def say_hello():
    print("你好你好我是sayhello")


if __name__ == "__main__":
    print("小明开发的模块")
    print(__name__)
    say_hello()

"""
不需要被导入时执行的测试代码


__name__属性是一个内置属性，记录着一个字符串
如果是被其他文件导入的,__name__就是模块名
如果是当前执行的程序__name__就是__main__

"""