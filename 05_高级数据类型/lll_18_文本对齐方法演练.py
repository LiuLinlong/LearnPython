# ljust rjust center
# 假设：以下内容是从网络上抓取
# 要求：顺序并且居中对齐输出以下内容
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))
    # ^J查看方法的介绍（macOS Pycharm） 参数为width,fillchar fillchar默认为英文空格，现在换为中文空格
# ljust和rjust的参数和center一样
for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "　"))
for poem_str in poem:
    print("|%s|" % poem_str.rjust(10, "　"))

"""
现在演示去除空格 strip （拖拽）
"""
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目\t",
        "\t更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, "　"))
