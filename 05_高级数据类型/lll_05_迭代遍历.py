name_list = ["zhangsan", "lisi", "wangwu", "sunwukong"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环中，数据都会保存在
my_name这个变量中，在循环体内部可以访问到当前这一次获取到的数据
"""
for my_name in name_list:
    print("我的名字叫%s" % my_name)

"""
列表的使用场景
    存储多个相同类型的数据（尽管Python中允许存储不同类型数据）
    通过迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作
"""
