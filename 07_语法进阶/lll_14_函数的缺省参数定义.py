def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学姓名
    :param gender: True男生False女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明")
print_info("老王")
print_info("小美", gender=False)

# 假设班上男生居多
# 在指定缺省参数的默认值时，应该使用最常见的值作为默认值
