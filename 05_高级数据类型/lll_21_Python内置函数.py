"""
公共方法
    Python内置函数
        len(item)   计算容器中元素个数
        del(item)   删除变量    del有两种方式    del的函数调用和命令调用
        max(item)   返回容器中最大值    如果是字典，只针对key比较，不针对值比较
        min(item)   返回容器中最小值    如果是字典，只针对key比较，不针对值比较
        cmp(item1, item2)   比较两个值， -1小于/ 0等于/ 1大于   字典之间不能比较（都无序了还比啥）
        Python3.X中取消了cmp函数，直接用比较运算符

        字符串比较'0'<'A'<'a' 【按照ASCII码】
"""
temp_dict = {"a": "z",
             "b": "y",
             "c": "x"}
# 从key来看 c 最大 a最小
# 从值来看 a的z最大 c的x最小
print(max(temp_dict))
print(min(temp_dict))
