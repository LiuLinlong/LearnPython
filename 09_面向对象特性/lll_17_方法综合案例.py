class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸吃掉你的脑子")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


Game.show_help()
Game.show_top_score()
game = Game("刘林龙")
game.start_game()
"""
实例方法——方法内部需要访问实例属性
    实例方法内部可以使用类名.访问类属性
类方法——方法内部只需要访问类属性
静态方法——方法内部，不需要访问实例属性和类属性
"""

