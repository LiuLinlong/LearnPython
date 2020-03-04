#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# 在这先运行一下，确保以后都直接运行这个
"""
TODO注释
#后一个空格TODO
提示自己代办
Pycharm左下角有TODO的汇总
"""
import cards_tools as ct

# 无限循环，由用户决定什么时候退出循环
while True:
    # 显示功能菜单
    ct.show_menu()
    action_str = input("请选择希望执行的操作：")
    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        print("您选择的操作是【%s】" % action_str)
        # 新增名片
        if action_str == "1":
            ct.new_card()
        # 显示全部
        elif action_str == "2":
            ct.show_all()
        # 查询名片
        elif action_str == "3":
            ct.search_card()
        # pass

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
        # pass
        # 开发程序时不希望现在编写内部代码，可以写一个pass关键字
        # 表示一个占位符，保证程序的代码结构正确！
        # 程序运行时，pass关键字不会执行任何操作

    # 其他内容输入错误，需要提示用户
    else:
        print("您输入有误，请重新输入")
