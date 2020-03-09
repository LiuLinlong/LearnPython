"""
如果父类之间存在同名的属性和方法，应该尽量避免使用多继承
"""


class A:
    def test(self):
        print("TestA func")

    def demo(self):
        print("DemoA func")


class B:
    def demo(self):
        print("DemoB func")

    def test(self):
        print("TestB func")


class C(A, B):
    pass


class D(B, A):
    pass


c = C()
c.test()
c.demo()
d = D()
d.test()
d.demo()
"""
Python中的MRO
Python中针对类提供了一个内置属性 __mro__可以查看方法的搜索顺序
MRO method_resolution_order，主要用于在多继承时判断方法、属性的调用路径
"""
print(C.__mro__)
print(D.__mro__)
"""
新式类和旧式（经典）类
object是Python为所有对象提供的基类，提供有一些内置的属性和方法，可以使用dir函数查看
新式类 以object类为基类的类   推荐使用
旧式类 不以object类为基类的类  不推荐使用
Python2.x内，如果没有指定父类，则不会以object作为基类
Python3.x内默认新式类
新式类或旧式类会影响方法的搜索路径
class A(object):
    pass
a = A()
dir(a)
"""
