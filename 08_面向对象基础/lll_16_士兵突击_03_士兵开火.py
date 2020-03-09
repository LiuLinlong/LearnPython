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

    def fire(self):
        # 1. check has gun
        # if self.gun == None:
        if self.gun is None:
            print("[%s] 还没有枪" % self.name)
            return
        # 2.say FIRE
        print("冲啊...[%s]" % self.name)
        # 3.add_bullet
        self.gun.add_bullet(50)
        # 4.make gun shoot
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")
# ak47.add_bullet(50)  # 自己不能开枪和加子弹
# ak47.shoot()

xusanduo = soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
# print(xusanduo.gun.model)

"""
身份运算符
用于比较两个对象的内存地址是否一致——是否是对同一个对象的引用
    is
    is not
注意 == 判断的是值
    is 判断的是引用 即使内容一样也会返回False
"""
