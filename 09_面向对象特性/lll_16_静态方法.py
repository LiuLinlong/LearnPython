"""
静态方法
如果需要在类中封装一个方法，这个方法：
    既不需要访问类属性或者调用类方法
    也不需要访问实例属性或者调用实例方法
这个时候可以把这个方法封装为一个静态方法
语法：
@staticmethod
def 静态方法名():  # 不需要self
    pass

"""

"""
调用
类名.静态方法

不需要创建实例
"""


class Dog:
    @staticmethod
    def run():
        print("RUN!")
