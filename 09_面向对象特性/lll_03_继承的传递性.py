# 继承具有传递性
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


xiaotianquan = XiaoTianQuan()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.bark()
xiaotianquan.fly()
