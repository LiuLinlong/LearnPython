"""
__str__方法
print是输出对象变量，默认情况下，会输出这个变量引用的对象是由哪一个类创建的对象，以及十六进制表示的在内存中的地址
如果在开发中，希望使用print函数输出对象变量时，能够打印自定义的内容，就可以利用__str__这个内置方法
注意：__str__方法IXUS返回一个字符串
"""


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s has come" % self.name)

    def __del__(self):
        print("%s has gone" % self.name)

    def __str__(self):
        return "我是小猫【%s】" % self.name


Tom = Cat("Tom")
print(Tom)
