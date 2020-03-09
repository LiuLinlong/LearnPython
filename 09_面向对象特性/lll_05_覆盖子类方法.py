"""
方法的重写
应用场景    父类的方法不能满足子类的序曲时，可以对方法进行重写(override)
1)覆盖父类方法
    在子类中定义同名方法
"""


class Animal:
    def eat(self):
        print("Eat!")

    def drink(self):
        print("Drink!")

    def run(self):
        print("Run!")

    def sleep(self):
        print("Sleep!")


class Dog(Animal):
    def bark(self):
        print("Bark!")


class XiaoTianQuan(Dog):
    def fly(self):
        print("Fly")

    # 如果子类中重写了父类的方法
    # 在使用子类对象调用方法时会调用重写的方法
    def bark(self):
        print("嘤嘤嘤(╥╯^╰╥)!")


class Test(XiaoTianQuan):
    def test_is_bark_change(self):
        self.bark()


xtq = XiaoTianQuan()
xtq.bark()

tt = Test()
tt.test_is_bark_change()
