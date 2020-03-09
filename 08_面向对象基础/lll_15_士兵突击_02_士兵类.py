"""
在定义属性时，如果不知道设置合适初始值，可以设置为None
    None关键字表示什么都没有
    表示一个空对象，没有方法和属性，是一个特殊的常量
    可以将None赋值给任何一个变量
"""


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print("【%s】突突突...[%d]" % (self.model, self.bullet_count))
        else:
            print("【%s】没有子弹了" % self.model)
            return


class soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None  # 新兵没有枪


ak47 = Gun("AK47")
ak47.add_bullet(50)
ak47.shoot()

xusanduo = soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun.model)

