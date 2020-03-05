def sum_numbers(*args):
    num = 0

    print(args)

    # 循环遍历
    for n in args:
        num += n

    return num


res = sum_numbers(1, 2, 3, 4, 5)  # 如果函数定义不加*，当元组的话，还得再加个()
print(res)
