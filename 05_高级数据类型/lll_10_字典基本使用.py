xiaoming_dict = {"name": "小明"}

# 取值
print(xiaoming_dict["name"])  # 取值都是[] 若key不存在会报错
# 增加、修改
# 如果key不存在会新增键值对，若key存在，会修改键值对
xiaoming_dict["age"] = 18
print(xiaoming_dict)

xiaoming_dict["name"] = "小小明"
print(xiaoming_dict)
# 删除 pop() 若key不存在，则会报错
xiaoming_dict.pop("age")
print(xiaoming_dict)
