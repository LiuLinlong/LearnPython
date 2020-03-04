"""
元组(Tuple)
表示多个元素组成的序列
在Python中有特定的应用场景
通常包含不同类型的数据
用()定义
索引从0开始

注意：元组的元素不能修改
"""
info_tuple = ("张三", 18, 1.75)
print(type(info_tuple))
print(info_tuple[0])

# 创建空元组
empty_tuple = ()
print(type(empty_tuple))
# 创建只有一个元素的元组
single_tup = (5)
print(type(single_tup))  # 提示为int

single_tuple = (5,)  # 后面跟一个 ,
print(type(single_tuple))

# 1.取值和取索引
print(info_tuple[1])
print(info_tuple.index("张三"))

# 2.统计计数
print(info_tuple.count(18))

print(len(info_tuple))
