"""
多值参数
需求：参数的个数是不确定的
Python有两种多值参数：
    参数名前增加一个 * 可以接收元组
    参数名前增加两个 * 可以接收字典

一般给多值参数命名时，习惯使用以下两个名字
    *args
    **kwargs
args全称arguments
kwargs全称 keyword arguments，可以记录键值对参数
"""


def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age="18岁")
