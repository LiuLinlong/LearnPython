"""
import 模块1 as 模块别名
模块别名应该符合大驼峰命名法
"""
import lll_01_测试模块1 as DogModule
import lll_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
cat = CatModule.Cat()

print(dog)
print(cat)

