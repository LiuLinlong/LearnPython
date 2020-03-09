"""
class 类名(父类名):
    pass
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
    # def eat(self):
    #     print("Eat!")
    #
    # def drink(self):
    #     print("Drink!")
    #
    # def run(self):
    #     print("Run!")
    #
    # def sleep(self):
    #     print("Sleep!")

    def bark(self):
        print("Bark!")


wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
"""
专业术语
Dog类是Animal类的子类，Animal类是Dog类的父类，Dog里从Animal类继承
Dog类是Animal类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生
"""
