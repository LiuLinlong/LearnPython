def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char: 分割线使用的字符
    :param times: 分割线重复的次数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


name = "刘林龙"

"""
使用模块中的函数
模块好比一个工具包
每个以py结尾的Python源代码文件都是一个模块
在模块中定义的全局变量、函数都是模块能够提供给外界直接使用的工具
"""
