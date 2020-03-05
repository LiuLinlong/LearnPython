def demo(num_list):
    print("用方法前")
    print(num_list)
    num_list.extend([1, 2, 3])  # 用方法直接修改列表内容
    # 注意append和extend的区别
    print("用方法后")
    print(num_list)
    print("函数运行完成")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
