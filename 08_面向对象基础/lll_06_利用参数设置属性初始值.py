class Cat():
    """这是一个猫类"""

    def __init__(self, new_name):
        # print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat("Tom")  # 自动调用初始化方法

print(tom.name)
tom.eat()

lazy_cat = Cat("大懒猫")
print(lazy_cat.name)
lazy_cat.eat()
"""
如果希望在创建对象的同时就设置对象的属性，可以对__init__方法进行改造
    1.把希望设定的属性值，定义成__init__方法的参数
    2.在方法内部使用 self.属性 = 形参 接收外部传递的参数
    3.创建对象时，使用类名（属性1, 属性2...)调用
"""
