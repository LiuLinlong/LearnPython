"""
元组和字典的拆包
在调用带有多值参数的函数时，如果希望
    将一个元组变量，直接传递给args
    将一个字典变量，直接传递给kwargs
拆包
    在元组变量前增加一个*
    在字典变量前增加两个*

"""


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}
# 拆包语法可以简化元组变量/字典变量的传递
demo(*gl_nums, **gl_dict)

demo(1, 2, 3, name="小明", age=18)

