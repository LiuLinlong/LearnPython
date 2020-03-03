i = 0
while i < 10:

    if i == 5:
        # 注意：在循环中如果使用 continue 关键字
        # 在使用关键字之前，需要确认循环的计数是否修改，否则可能会死循环
        i += 1  # continue后会直接跳过当前循环的后续代码 包括 i += 1
        continue
    print(i)

    i += 1
