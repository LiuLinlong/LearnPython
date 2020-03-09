"""
给对象增加属性
在Python中，要给对象设置属性非常容易，但是不推荐使用
    因为：对象属性的封装应该在类的内部
只需要在类的外部代码中直接通过 . 设置一个属性即可【不推荐】
"""

"""
利用self在类封装的方法中输出对象属性
哪一个对象调用的方法，self就是哪一个对象的引用
在类封装的方法内部，self就表示当前调用方法的对象自己
调用方法时，程序员不需要传递self参数
在方法内部
    可以通过 self. 访问对象的属性
    也可以通过 self. 调用其他的方法
"""


class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


# 创建猫对象
tom = Cat()
# 利用调试工具看有没有被创建name属性，当然也可以看见self的内容
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

"""
初始化方法
    原有代码的问题
"""
