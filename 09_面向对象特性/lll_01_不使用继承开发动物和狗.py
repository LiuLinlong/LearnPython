"""
面向对象的三大特性：
    封装  根据职责将属性和方法封装到一个抽象的类中
    继承  实现代码的重用，相同的代码不需要重复的编写
    多态  不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度

单继承
    继承的概念   子类拥有父类的所有方法和属性
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


class Dog:
    def eat(self):
        print("Eat!")

    def drink(self):
        print("Drink!")

    def run(self):
        print("Run!")

    def sleep(self):
        print("Sleep!")

    def bark(self):
        print("Bark!")


class XiaoTianQuan:
    def eat(self):
        print("Eat!")

    def drink(self):
        print("Drink!")

    def run(self):
        print("Run!")

    def sleep(self):
        print("Sleep!")

    def bark(self):
        print("Bark!")

    def fly(self):
        print("Fly!")


# 如果这时需要修改动物类的方法，那么狗、哮天犬相应的也要改变
wangcai = Animal()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()

erha = Dog()
erha.eat()
erha.drink()
erha.run()
erha.sleep()
erha.bark()
