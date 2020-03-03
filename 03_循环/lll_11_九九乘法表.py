row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="    ")  # 可以用\t让它垂直对齐
        col += 1
    print("")
    row += 1
