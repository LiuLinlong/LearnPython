class Tool:
    cnt = 0

    def __init__(self, name):
        self.name = name
        Tool.cnt += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# print(Tool.cnt)

tool1.cnt = 99

print(tool1.cnt)

print("==> %d" % Tool.cnt)

