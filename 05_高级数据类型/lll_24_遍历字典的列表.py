"""
for-else应用场景
在迭代遍历嵌套的数据类型时，例如 一个列表包含了多个字典
需求：要判断 某一个字典中 是否存在 指定的 值
    如果存在，提示并且退出循环
    如果不存在，在循环整体结束后，希望得到一个统一的提示
"""

# 学员列表中找人
students = [
    {"name": "小强"},
    {"name": "小美"}
]
find_name = input("请输入要查找的学生姓名：")
for stu_dict in students:
    if stu_dict["name"] == find_name:
        print("找到了%s" % find_name)
        # 已经找到了，所以应该退出循环
        break
else:
    # 没有的时候给予统一的回复
    print("不好意思，没有找到%s" % find_name)

print("循环结束")
