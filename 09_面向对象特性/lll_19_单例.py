class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)

"""
单例
    定义一个类属性，初始值为None，用于记录单例的引用
    重写__new__方法
    如果类属性is None，调用父类方法分配空间，并在类属性记录结果
    返回类属性中记录的对象引用
"""
