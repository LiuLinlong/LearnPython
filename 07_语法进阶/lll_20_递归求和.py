def sum_numbers(num):
    # 1.exit
    if num == 1:
        return 1

    # 2.数字累加 num+（1+2+3+...+num-1)
    # 假设 sum_numbers 能够正确处理 1...num-1
    temp = sum_numbers(num - 1)
    return num + temp
    # return num + sum_numbers(num - 1)


res = sum_numbers(998)
print(res)
