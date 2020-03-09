class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s Jump Up And Down" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s Fly to The Sky and Jump Up And Down" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s plays games happily with %s" % (self.name, dog.name))
        dog.game()


# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)
