"""
私有属性和私有方法
应用场景
    对象的某些属性或方法只希望在对象的内部被使用，而不希望在外部被访问到
    私有属性就是对象不希望公开的属性
    私有方法就是对象不希望公开的方法
定义方式
    在定义属性或方法时，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法

"""


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部是可以使用对象的私有属性的
        print("%s的年龄是%d岁" % (self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性在外界不能访问
# print(xiaofang.__age)

# 私有方法同样不允许在外界使用
# xiaofang.__secret()

