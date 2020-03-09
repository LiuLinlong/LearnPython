"""
实例
__init__定义实例属性
实例方法(self)
实例：创建出来的对象
创建对象的动作叫做实例化
每个对象都有自己独立的内存空间，保存各自不同的属性
多个对象的方法，在内存中只有一份，在调用方法时，需要把对象的引用传递到方法内部

类是一个特殊的对象
Python中一切皆对象
class AAA:定义的类属于类对象
obj1 = AAA()属于实例对象
在程序运行时，类同样会被加载到内存
类对象有自己的属性和方法
    类属性
    类方法
类名. 的方式访问类的属性或者调用类的方法

类属性就是给类对象定义的属性
通常用来记录与这个类有关的特征
类属性不会用于记录具体对象的特征

示例需求：
    定义一个工具类
    每个工具都有自己的name
    需求————知道使用这个类创建了多少个工具对象
"""


class Tool:
    cnt = 0

    def __init__(self, name):
        self.name = name
        Tool.cnt += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
print(Tool.cnt)
