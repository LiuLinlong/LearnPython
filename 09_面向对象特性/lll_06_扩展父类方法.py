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
        # 1.针对子类特有的需求，编写代码
        print("Bark as a God!")
        # 2.使用super()调用父类的方法
        # super().bark()
        # 父类名.方法(self)
        # 注意如果误写作子类调用方法(self)，会形成递归调用，死循环
        Dog.bark(self)
        # 3.增加其他子类的代码
        print("I'm a God!")


xtq = XiaoTianQuan()
xtq.bark()

"""
父类方法重写实现2——父类方法的扩展
    子类的方法实现中包含父类方法
扩展
    1.在子类中重写父类的方法
    2.在需要的位置使用super.()父类方法来调用父类方法的执行
    3.代码其他的位置针对子类的需求，编写子类特有的代码实现
关于super
    一个特殊的类
    super()其实就是使用super创建一个对象
调用父类方法的其他方式
    在python2.x中不支持super
    父类名.方法(self)
    不推荐

"""
