"""
字符串的切片
切片方法适用于 字符串、列表、元组（不能字典，因为字典无序，没有索引的概念）
    切片使用索引值来限定范围，从一个大的字符串中切出小的字符串
    列表和元组都是有序的集合，都能够通过索引值获取到对应的数据
    字典是一个无序的集合，是使用键值对保存数据
语法格式
    字符串[开始索引:结束索引:步长]  # 步长就是多久切一刀
注意：指定区间属于左闭右开（其实就是切的地方在这个索引键的前面）

顺序索引——第一个位置是1
倒序索引——最后一个位置对应-1    重要!!
想要切到末尾可以不指定结束索引
"""
num_str = "0123456789"
# 截取2~5
print(num_str[2:6])
# 截取从2到末尾
print(num_str[2:])
# 截取从开始到5
print(num_str[:6])
# 截取完整字符串
print(num_str[:])
# 从开始位置，每隔一个字符截取字符串
print(num_str[::2])
# 从索引1开始，每隔一个取一个
print(num_str[1::2])
# 截取从2~末尾-1的字符串
print(num_str[2:-1])
# 截取字符串末尾两个字符
print(num_str[-2:])
# 字符串的逆序（面试题）
print(num_str[-1::-1])
