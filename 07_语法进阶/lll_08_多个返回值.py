"""
函数参数和返回值的作用
定义函数时，是都接收参数、是否返回结果由需求决定
"""


# 一个函数返回多个结果


def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = 39
    witness = 50
    print("测量结束")
    # 元组-可以包含多个数据，因此可以用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp, witness)
    return temp, witness


# 元组
result = measure()
print(result)

# 需要单独处理温度或湿度 - 不方便
print(result[0])
print(result[1])  # 准确记录索引太麻烦了

# 如果函数返回类型是元组，同时希望单独处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数必须和元组中元素的个数保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
