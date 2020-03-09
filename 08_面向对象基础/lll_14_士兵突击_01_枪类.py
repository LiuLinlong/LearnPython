"""
一个对象的属性可以是另一个类创建的对象

需求
    士兵xsd有一把AK47
    士兵可以开火
    枪可以发射子弹
    枪可以装填子弹——增加子弹数量
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


ak47 = Gun("AK47")
ak47.add_bullet(50)
ak47.shoot()

