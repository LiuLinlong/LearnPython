def demo(num, num_list, str_list):
    print("Function Starts")
    num += num
    # 列表变量使用+=不会想家再赋值
    # 而是调用了列表的extend整合两个列表的方法，不会修改引用
    num_list += num_list
    # 而 = +这个拆分操作就是正常的修改引用，不会影响实参
    str_list = str_list + str_list
    print(num)
    print(num_list)
    print(str_list)
    print("Finished")


gl_num = 9
gl_list = [1, 2, 3]
gl_str = ["Hello", "Python"]
demo(gl_num, gl_list, gl_str)
print(gl_num)
print(gl_list)
print(gl_str)
