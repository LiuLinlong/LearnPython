name_list = ["张三", "李四", "王五", "张三"]
# len
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)  # 3个元素，但是索引到2

# count
print("张三出现了 %d 次" % name_list.count("张三"))

# 从列表中删除数据
name_list.remove("张三")
# Remove first occurrence of value.
# Raises ValueError if the value is not present.
print(name_list)
