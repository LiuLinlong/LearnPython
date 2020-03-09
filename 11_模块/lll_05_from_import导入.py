from lll_01_测试模块1 import Dog
from lll_02_测试模块2 import say_hello
from lll_01_测试模块1 import say_hello as M1_say_hello


say_hello()
wangcai = Dog()
print(wangcai)
M1_say_hello()


# 在两个模块中导入了同名函数，后导入的会覆盖先导入的
# 一旦发现冲突，可以使用as来为其中一个函数起别名
