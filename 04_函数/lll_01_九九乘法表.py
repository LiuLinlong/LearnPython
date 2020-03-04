"""
函数的快速体验
函数的使用包含两个步骤：
    1. 定义函数 —— 封装 独立的功能
    2. 调用函数 —— 享受 封装 的成果
"""


def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")  # 可以用\t让它垂直对齐
            col += 1
        print("")
        row += 1
