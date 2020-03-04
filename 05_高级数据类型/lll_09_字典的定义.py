"""
字典
除列表以外最灵活的数据类型

列表存储 有序 的对象集合
字典存储 无序 的对象集合
字典用 {} 定义
字典使用 键值对 存储数据，键值对之间用 , 分隔
    键 key 是索引
    值 value 是数据
    键和值之间用 : 分隔
    键必须是唯一的
    值可以取任何数据类型，但 键 只能使用 字符串、数字或元组

    xiaoming = {"name" : "xiaoming",
                "age" : 18,
                "gender" : True,
                "height" : 1.75}

应用场景
    存储物体的信息
"""
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}
# 字典是无序的数据集合
# 通常使用print得到的结果和存储顺序不一样
print(xiaoming)
