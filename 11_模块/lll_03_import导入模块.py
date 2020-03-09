import lll_01_测试模块1
import lll_02_测试模块2

lll_01_测试模块1.say_hello()
lll_02_测试模块2.say_hello()

dog = lll_01_测试模块1.Dog()
print(dog)

cat = lll_02_测试模块2.Cat()
print(cat)

"""
模块的导入方法
    import导入
        import module1, module2  # 不推荐 PEP8不推荐

        import module1
        import module2
"""