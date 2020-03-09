"""
单例
单例设计模式
设计模式
    设计模式是前人工作的总结和提炼，通常，被人们广泛流传的设计模式都是针对某一特定问题的成熟的解决方案
    使用设计模式是为了可重用代码、让代码更容易被他人理解、保证代码的可读性
单例设计模式
    目的——让类创建的对象，在系统中只有唯一的实例
    每一次执行类名()返回的对象，内存地址是相同的

"""
"""
__new__方法是一个object基类提供的静态方法
作用
    在内存中为对象分配空间
    返回对象的引用
将引用作为第一个参数传递给__init__方法
    重写__new__方法的代码非常固定
    重写new方法一定要 return super().__new__(cls) # 这是返回对象的引用，init才能工作
"""


class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象时__new__方法会自动调用
        print("创建对象，分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)
        return instance

        # 返回对象的引用

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)
