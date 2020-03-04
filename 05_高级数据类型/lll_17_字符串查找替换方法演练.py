hello_str = "hello world"

# 1.判断是否以指定字符串开始
print(hello_str.startswith("h"))
print(hello_str.startswith("Hello"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("D"))
print(hello_str.endswith("d"))

# 3.查找指定字符串
print(hello_str.find("llo"))  # 输出开始出现的index 与index的效果一样，区别见下面
print(hello_str.find("abc"))  # 不存在时index会报错，find会-1

# 4.替换字符串
# replace执行完成后会返回一个新的字符串
# 但不会修改字符串内容！！！
print(hello_str.replace("world", "python"))
print(hello_str)
