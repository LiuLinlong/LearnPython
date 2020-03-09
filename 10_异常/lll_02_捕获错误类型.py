try:

    num = int(input("请输入一个整数："))

    res = 8 / num

    print(res)

except ZeroDivisionError:
    print("除数不可以是0！")

except ValueError:
    print("请输入一个正确的整数！！！")

"""
错误类型就是报错的第一个单词
"""
