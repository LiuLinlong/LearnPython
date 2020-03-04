"""
完整的for循环语法

for 变量 in 集合:
    循环体代码
else:
    循环体内没有通过break退出循环，就会执行
"""
for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else下方的代码就不会被执行
    print("执行了else")
print("循环结束")
