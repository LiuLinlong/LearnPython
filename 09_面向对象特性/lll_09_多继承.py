"""
多继承——子类有多个父类，并且具有所有父类的属性和方法
语法
class 子类名(父类名1, 父类名2...)
    pass
"""


class A:
    def test(self):
        print("Test func")


class B:
    def demo(self):
        print("Demo func")


class C(A, B):
    pass


c = C()
c.test()
c.demo()
