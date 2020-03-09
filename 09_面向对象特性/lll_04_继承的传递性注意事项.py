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


class Cat(Animal):
    def catch(self):
        print("Catch mouse!")


xiaotianquan = XiaoTianQuan()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.bark()
xiaotianquan.fly()

# xiaotianquan.catch()
