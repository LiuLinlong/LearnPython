"""
【我就该用Markdown语法记笔记，然后在pycharm安一个Markdown插件】
运算符
运算符             Python表达式               结果                      描述          支持的数据类型
+               [1, 2]+[3, 4]           [1, 2, 3, 4]                合并          字符串、列表、元组
*               ["Hi!"] * 4             ["Hi", "Hi", "Hi", "Hi"]    重复          字符串、列表、元组
in              3 in (1, 2, 3)          True                        元素是否存在    字符串、列表、元组、字典
not in          4 not in (1, 2, 3)      True                        元素是否不存在   字符串、列表、元组、字典
> >= == < <=    (1, 2, 3) < (2, 2, 3)   True                        元素比较        字符串、列表、元组

注意：in 用于字典时，判断的是字典的键
"""
# 除了+以外，append()和extend()方法都可以追加内容，但注意区别
t_list = [1, 2, 3, 4, 5]
t_list += [6]
print(t_list)
# extend为列表和数值时
t_list.extend([7, 8])
print(t_list)
# t_list.extend(9)  # 会报错TypeError: 'int' object is not iterable 所以必须是列表
# print(t_list)

# append是数值和列表时候
t_list.append(9)
print(t_list)
t_list.append([10, 11])  # 把[10, 11]作为一个列表插入到列表内
print(t_list)

"""
成员运算符包含
    in 
    not in
"""
