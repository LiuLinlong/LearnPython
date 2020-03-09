class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f平米" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f平米[剩余：%.2f平米]\n家具：%s"
                % (self.house_type,
                   self.area,
                   self.free_area,
                   self.item_list))

    # Pycharm能自动的将一对括号内部的代码连接在一起

    def add_item(self, item):
        print("要添加 %s" % item)


bed = HouseItem("席梦思", 4)
# print(bed)
chest = HouseItem("衣柜", 2)
# print(chest)
table = HouseItem("餐桌", 1.5)
# print(table)

my_home = House("四室一厅", 140)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
