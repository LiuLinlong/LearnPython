has_ticket = True
knife_length = 10
if has_ticket:
    print("Ready to SafeCheck")
    if knife_length > 20:
        print("You take a knife whose length is %dcm, and it is over 20cm!" % knife_length)
        print("You can't come in")
    else:
        print("You have take the SafeCheck")
        print("Please come in")
else:
    print("Please buy a ticket first")

"""
command + /     多行注释
多选 + Tab        多行向右缩进
多选 Shift + Tab  多行向左缩进
"""