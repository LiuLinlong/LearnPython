"""
01.封装
封装是面向对象编程的一大特点
面向对象编程的第一步——将属性和方法封装到一个抽象的类中
外界使用类创建对象，然后让对象调用方法
对象方法的细节都被封装在类的内部

02.小明爱跑步
需求：
    小明体重75.0公斤
    小明每次跑步会减肥0.5公斤
    小明每次吃东西体重会增加1公斤
"""


class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def run(self):
        print("%s爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1

    def __str__(self):
        return "我的名字是%s 体重是 %.1f 公斤" % (self.name, self.weight)


xiaoming = Person("小明", 75.0)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
