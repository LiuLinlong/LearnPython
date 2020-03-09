"""
对象的内置方法
__del__方法
在Python中，
    当使用类名()创建对象时，为对象分配完空间后，自动调用__init__方法
    当一个对象被从内存销毁前，再做一些事情，可以考虑__del__方法
生命周期
    当一个对象调用类名()创建，生命周期开始
    一个对象的__del__方法一旦被调用，生命周期结束
    在对象的生命周期内可以访问对象的属性，或着让对象调用方法
"""


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s has come" % self.name)

    def __del__(self):
        print("%s has gone" % self.name)


# Tom是全局变量，所以当全部代码执行完内存才会被释放
Tom = Cat("Tom")
print(Tom.name)
# del关键字可以删除一个对象
# del Tom
print("-" * 50)
