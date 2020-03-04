name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
print(name_list[2])
# 取索引——知道数据的内容，想知道位置
# 注意如果数据不在列表中会报错
print(name_list.index("lisi"))

# 2.修改
name_list[1] = "李四"  # 注意列表的索引超出range会报错
print(name_list)

# 3.增加
name_list.append("王小二")  # 向列表末尾追加
print(name_list)

name_list.insert(1, "小猫咪")  # 可以在列表的指定索引位置插入数据
print(name_list)

temp_list = ["孙悟空", "猪八戒", "沙和尚"]
name_list.extend(temp_list)  # 把其他列表的内容追加到当前列表的末尾
print(name_list)

# 4.删除
# pop remove clear
name_list.remove("wangwu")  # 删除指定的数据
print(name_list)
name_list.pop()  # 默认把列表最后一个数据删除
print(name_list)
name_list.pop(3)  # 可指定要删除的元素的索引
print(name_list)
name_list.clear()  # 清空列表
print(name_list)

"""
List列表
python中使用最频繁的数据类型（类似于数组）
专门存储一串信息
用[]定义，数据之间用,分隔
索引从0开始
超出索引（index range）范围会报错（下标）列表[索引值] List[index]
len(列表) 获取列表的长度 n+1     [0 1 2 3 ... n]
列表.count(data)获取data出现的次数
"""

"""
列表的常用操作（共11个操作（方法））
定义一个列表，然后列表. 然后按tab就可获得所有操作
"""
