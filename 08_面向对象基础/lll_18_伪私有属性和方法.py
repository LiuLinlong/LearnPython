"""
伪私有属性和私有方法（科普）
tips:在日常开发中不要使用这种方式访问对象的私有属性或私有方法
在Python中并没有真正意义的私有
    在给属性、方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
    处理方式：在名称前加上 _类名 => _类名__名称
"""
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部是可以使用对象的私有属性的
        print("%s的年龄是%d岁" % (self.name, self.__age))


xiaofang = Women("小芳")
# print(xiaofang.__age)  # 报错
print(xiaofang._Women__age)
# xiaofang.__secret()  # 报错
xiaofang._Women__secret()
