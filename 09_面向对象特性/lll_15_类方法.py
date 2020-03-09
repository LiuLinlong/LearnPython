"""
类方法和静态方法
语法：
@classmethod
def 类方法名(cls):
    pass

由哪一个类调用的方法，cls就是那个类的引用
在方法内部
    可以通过cls.访问类的属性
    可以使用cls.调用其他类方法

"""


class Tool:
    cnt = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.cnt)

    def __init__(self, name):
        self.name = name
        Tool.cnt += 1


tool1 = Tool("锤子")
tool2 = Tool("榔头")
Tool.show_tool_count()
