"""
函数的参数 进阶
可变参数和不可变参数
    在函数内部，针对参数使用赋值语句，并不会影响实参
    下面开始演示
"""


# def demo(num):
#     print("函数内部的代码")
#     num = 100
#     print(num)
#     print("函数执行完成")
#
#
# gl_num = 99
# demo(gl_num)
# print(gl_num)
# """
# num是复制了一张贴在99上的gl_num的标签
# 执行函数时候，把num的标签又贴到了100身上
# 全程 gl_num 的标签就没从99上摘下来过
# """


def demo(num, num_list):
    print("函数内部的代码")
    num = 100
    num_list = [1, 2, 3]

    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
