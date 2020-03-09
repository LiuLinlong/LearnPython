"""
之前已经实现了，无论创建多少个对象都只返回第一次被创建对象的引用
但是：初始化方法仍会被调用
需求：让初始化动作只执行一次
"""


class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("初始化播放器")
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
