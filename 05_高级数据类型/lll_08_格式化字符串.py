"""
元组的应用场景
    作为函数的参数和返回值，一个函数可以接收任意多个参数 或者 一次返回多个数据
    格式字符串，格式化字符串 print("dcdc%d%s" % (a, b))这个(a, b)就是一个元组
    让列表不可以被修改，以保护数据安全
"""

# 格式化字符串后的()就是元组
info_tuple = ("小明", 18, 1.75)
print("%s 年龄是 %d 岁 身高是 %.2f" % ("小明", 18, 1.75))
print("%s 年龄是 %d 岁 身高是 %.2f" % info_tuple)  # 我试了，list是不行的，会报错
# 用元组拼接生成一个新字符串
info_str = "%s 年龄是 %d 岁 身高是 %.2f" % info_tuple
print(info_str)
print(type(info_str))

"""
tuple() 将list转换为tuple
list()  将tuple转换为list
"""
