# 完成五行的内容的简单输出
# 分析每行内部的*如何处理
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")  # 每行输出结束后添加一个换行
    row += 1
