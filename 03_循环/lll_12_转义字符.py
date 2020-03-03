row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    print("")
    row += 1

"""
字符串中的转义字符
    \\  反斜杠符号
    \'  单引号
    \"  双引号
    \n  换行
    \t  横向制表符
    \r  回车
"""
print("1  2  3")
print("10  20  30")
print("1\t2\t3")
print("10\t20\t30")

print("Hello Python")
print("Hello\n Python")

print("Hello\"Hello")
