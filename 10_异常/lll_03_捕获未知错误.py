try:

    num = int(input("请输入一个整数："))

    res = 8 / num

    print(res)

except ZeroDivisionError:
    print("除数不可以是0！")

except Exception as result:
    print("未知错误 %s" % result)

"""
捕获未知错误
在开发时，预测到所有可能出现的错误是有一定难度的
如果希望程序无论什么错误出现，都不会因为Python解释器抛出异常而被终止，可以再增加一个except

except Exception as result:
    print("未知错误 %s" % result)
"""

"""
完整代码
try:
    # 尝试执行的代码
    pass
except  ErrorType1:
    pass
except  ErrorType2:
    pass
except  (ErrorType3, ErrorType4)
    pass
except Exception as result:
    print(result)
else:
    没有异常才会执行的代码
finally:
    # 无论是否有异常都会执行的代码
    pass
    
"""