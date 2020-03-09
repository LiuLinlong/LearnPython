"""
包是一个包含多个模块的特殊目录
目录下有一个特殊的文件 __init__.py
包名的命名方式和变量名一致，小写字母和_

import 包名 可以一次性导入包中所有的模块
"""


import lll_message
lll_message.send_message.send("Hello")
txt = lll_message.receive_messsage.receive()
print(txt)

