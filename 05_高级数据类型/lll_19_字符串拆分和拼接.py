"""
string.split(str="", num)   以str为分隔符拆分string，如果num有指定值，则仅分隔num+1个子字符串，str默认包含'\r''\t''\n'和空格
string.join(seq)    以string作为分隔符，将seq中所有元素（的字符串表示）合并为一个新的字符串
"""

# 假设：以下内容是从网络上抓取的
# 要求：
# 1.将字符串中的空白字符全部去掉
# 2.再使用 " " 作为分隔符，拼接成一个整齐的字符串
poem_str = "登鹳雀楼 \t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t 欲穷千里目 \t\t 更上一层楼"
print(poem_str)
# 1.拆分字符串
poem_list = poem_str.split()  # ctrl+J查看帮助文档（macOS的Pycharm）
print(poem_list)
# 2.合并字符串
poem_res = " ".join(poem_list)
print(poem_res)
