

#打印的格式化：format

# name = input("请输入姓名：")
# age  = input("请输入年龄：")
# sex  = input("请输入性别：")
# id   = input("请输入身份证号")
# high = input("请输入身高：")
# weight = input("请输入体重：")
#
# info = '''
# ----------------个人信息----------------
# 姓名:{name}
# 性别:{sex}
# 年龄:{age}
# 身份证号:{id}
# ---------------------------------------
# '''
#
# print(info.format(name=name,sex=sex,age=age,id = id))

#随机数:random模块：random.randint

# import random
# num = random.randint(110,550)
# print(num)


import random
num = random.randint(0,300)
jinbi = 2000
i = 0
count = 0

while i <= 10:
    jinbi = jinbi - 200
    count = count + 1
    shuru = input("请输入您要猜的数字：")
    shuru = int(shuru)
    if num < shuru:
        print("输入的数字太大了","金币剩余：",jinbi)
    elif num > shuru:
        print("您输入的数字太小了","金币剩余：",jinbi)
    elif jinbi == 0:
        print("您的金币用完了，请充值")
        break
    else:
        mani = (jinbi + 5000)
        print("恭喜您猜对了，奖励您5000金币",'输入次数：',count,"剩余金币：",mani)
        jixu =print( input("是否继续：(y/n)"))
        if jixu == 'n':
            print("欢迎下次再来")
            break

        else:
            num = random.randint(0, 300)
            jinbi = mani



