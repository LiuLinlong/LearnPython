"""
初始化方法
当使用类名()创建对象时，会自动执行以下操作
    1.为对象在内存中分配空间——创建对象
    2.为对象的属性设置初始值——初始化方法init
这个初始化方法就是 __init__ 方法， __init__ 是对象的内置方法，专门用来定义一个类具有哪些属性的方法
"""


class Cat():
    """这是一个猫类"""

    def __init__(self):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat()  # 自动调用初始化方法

print(tom.name)
tom.eat()
