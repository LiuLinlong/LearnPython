"""
摆放家具
需求
    1.房子(House)有户型，总面积和家具名称列表
        新房子没有任何家具
    2.家具有(HouseItem)名字和占地面积，其中
        席梦思(bed)占地4平米
        衣柜(chest)占地2平米
        餐桌(table)占地1.5平米
    3.以上三件家具添加到房子中
    4.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

被使用的类先开发，因为House类需要使用到HouseItem类，所以，先开发HouseItem类
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f平米" % (self.name, self.area)


bed = HouseItem("席梦思", 4)
print(bed)
chest = HouseItem("衣柜", 2)
print(chest)
table = HouseItem("餐桌", 1.5)
print(table)
