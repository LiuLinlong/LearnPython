"""
确定需求
分解步骤
逐步编码
"""
# 如果需求某一步不能完成，那就先固定，完成后面的代码，使整个项目先完成

# 导入随机工具包
# 导入工具包的时候应该将导入语句放在文件的顶部，以便于下方代码在任何需要的时候使用工具包中的工具
import random
# 从控制台输入要出的拳
player = int(input("请输入您要出的拳    石头（1）/剪刀（2）/布（3）："))

# 电脑随机出拳
"""
随机数的处理
import random
random.randint(a,b) 返回[a,b]之间的一个整数(包含起始和结束)
"""

computer = random.randint(1, 3)

print("玩家选择的拳头是： %d - 电脑出的拳是 %d" % (player, computer))

# 比较胜负
# if ()or()or():
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):  # 通过加条件外()实现可以换行
    print("玩家胜利")
elif player == computer:
    print("心有灵犀，继续吧")
else:
    print("我不服！继续！")
