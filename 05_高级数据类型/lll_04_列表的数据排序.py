"""
升序排序 sort()
降序排序 sort(reverse==True)
逆序  reverse()
"""
import keyword

name_list = ["zhangkaizheng", "bianhuaqing", "lvhongliang", "liulinlong", "zhangshengzhi", "liuweixin"]
print(name_list)
num_list = [6, 1, 5, 7]
print(num_list)

# name_list.sort()
# print(name_list)
# num_list.sort()
# print(num_list)

# name_list.sort(reverse=True)
# print(name_list)
# num_list.sort(reverse=True)
# print(num_list)

name_list.reverse()
print(name_list)
num_list.reverse()
print(num_list)

"""
关键字后面不需要()

函数
    函数名(参数)
    函数名需要背
方法
    对象.方法名(参数)
    只针对当前对象，用.检索就好
关键字
    关键字后不需要括号

"""
print(len(keyword.kwlist))

"""
循环遍历【python中有迭代遍历 iteration遍历】
使用 for
"""
