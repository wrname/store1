#li = ['猫','狗','老鼠','老虎']

#添加
#li.append("火鸡")
#li.append("狮子")

#修改
#li[0] = "大象"
#li[3] = "犀牛"

#查询
# data = li[0]
# data = li[3]

#删除
#del li[2]
#del li[3]
#print(li)


#购物商城
import random

# yes = print("是否获取优惠卷：是或否")
# if yes == "是":
#     p = random.randint(0, 5)
#     if p > 5 :
#         print("恭喜您获得老干妈优惠卷")
#     else:
#         print("恭喜您获得联想电脑优惠卷")
# else:
#     pass

shop =[
    ["劳力士",20000],
    ["手机",12000],
    ["联想电脑",6000],
    ["零食",20],
    ["老干妈",50]
]
#输入我的金额
maney = input("请输入您的金额：")
#强制转为数字格式
maney = int(maney)
#购物车
mycart = []
#随机获取优惠卷
you = input("是否获取优惠卷：是/否")
if you == "是":
    num = int(random.randint(0,1))
    if num == 0:
        print("恭喜您获得老干妈优惠卷")
    else:
        print("恭喜您获取联想电脑优惠卷")
else:
    print("你确定不要优惠卷吗")

#买东西
i = 0
while i <= 20:
    #展示商品
    for key,value in enumerate(shop):
        print(key,value)
    #输入您要的商品
    chose = input("请输入你想要的商品编号：")
    #判断商品是否存在
    if chose.isdigit():#判断输入的字符转为数字
        chose = int(chose)
        mycart.append(shop[chose][1])
        if chose > 5:
            print("您输入的商品不存在，请从新输入")
        elif chose == 2:
            maney = maney - (shop[chose][1]) * 0.1
            print("恭喜，成功添加到购物车！您的余额还剩：,",maney,"已使用联想电脑优惠卷")
        elif chose == 4:
            maney = maney - (shop[chose][1]) * 0.7
            print("恭喜，成功添加到购物车！您的余额还剩：,",maney,"已使用老干妈优惠卷")
        elif maney < shop[chose][1]:
            print("您的余额不足")
        else:
            #将商品添加到购物车
            mycart.append(shop[chose])
            maney = maney - shop[chose][1]
            print("恭喜，成功添加到购物车！您的余额还剩：",maney)


    elif chose == "q" or chose == "Q":
        print("成功退出商品界面，欢迎下次光临")
    else:
        print("输入的信息有误，请重新输入")
        break
    i = i+1







