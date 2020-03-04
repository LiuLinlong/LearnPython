"""
函数的返回值是函数的结果
return来返回结果
"""


def sum_2_num(num1, num2):
    """对两个数字的求和"""
    res = num1 + num2
    return res
# return 表示返回，return下方的函数体内代码不会被执行到


sum_result = sum_2_num(1, 2)

print("计算结果为%d" % sum_result)