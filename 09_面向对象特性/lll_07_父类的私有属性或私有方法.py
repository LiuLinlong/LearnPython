"""
父类的私有属性和私有方法
子类对象不能在自己的方法内部 ，直接访问父类的私有属性或私有方法
子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("Private function %d %d" % self.num1, self.__num2)


class B(A):
    def demo(self):
        # 1.不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 2.调用父类的私有方法
        # self.__test()
        pass


b = B()
print(b)
# 在外界不能直接访问对象的私有属性和私有方法
b.demo()
