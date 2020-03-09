"""
原有代码的问题，如果先调用方法，再添加属性会报错
"""


class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


tom = Cat()

tom.eat()
tom.drink()
tom.name = "Tom"
print(tom)

lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
