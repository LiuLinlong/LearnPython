class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("Private function %d %d" % (self.num1, self.__num2))

    def pub_func(self):
        # print("Parents Pub_func %d" % self.__num2)
        self.__test()


class B(A):
    def demo(self):
        # 1.不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 2.调用父类的私有方法
        # self.__test()
        # 3.访问父类的公有属性
        print(self.num1)
        # 4.访问父类的公有方法
        self.pub_func()


b = B()
print(b)
# 在外界不能直接访问对象的私有属性和私有方法
b.demo()

