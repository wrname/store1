import random

def shopping():
    shop = [
        ["劳力士", 20000],
        ["手机", 12000],
        ["联想电脑", 6000],
        ["零食", 20],
        ["老干妈", 50]
    ]
    # 输入我的金额
    maney = input("请输入您的金额：")
    # 强制转为数字格式
    maney = int(maney)
    # 购物车
    mycart = []
    # 随机获取优惠卷
    you = input("是否获取优惠卷：是/否")
    if you == "是":
        num = int(random.randint(0, 1))
        if num == 0:
            print("恭喜您获得老干妈优惠卷")
        else:
            print("恭喜您获取联想电脑优惠卷")
    else:
        print("你确定不要优惠卷吗")

    # 买东西
    i = 0
    while i <= 20:
        # 展示商品
        for key, value in enumerate(shop):
            print(key, value)
        # 输入您要的商品
        chose = input("请输入你想要的商品编号：")
        # 判断商品是否存在
        if chose.isdigit():  # 判断输入的字符转为数字
            chose = int(chose)
            mycart.append(shop[chose][1])
            if chose > 5:
                print("您输入的商品不存在，请从新输入")
            elif chose == 2:
                maney = maney - (shop[chose][1]) * 0.1
                print("恭喜，成功添加到购物车！您的余额还剩：,", maney, "已使用联想电脑优惠卷")
            elif chose == 4:
                maney = maney - (shop[chose][1]) * 0.7
                print("恭喜，成功添加到购物车！您的余额还剩：,", maney, "已使用老干妈优惠卷")
            elif maney < shop[chose][1]:
                print("您的余额不足")
            else:
                # 将商品添加到购物车
                mycart.append(shop[chose])
                maney = maney - shop[chose][1]
                print("恭喜，成功添加到购物车！您的余额还剩：", maney)


        elif chose == "q" or chose == "Q":
            print("成功退出商品界面，欢迎下次光临")
        else:
            print("输入的信息有误，请重新输入")
            break
        i = i + 1

def city():
    data = {
        "北京":{
            "昌平":{
                "十三陵":["十三陵水库","沙河水库"],
                "高校":["北京邮电大学","中央戏剧学院","北京师范大学","华北电力大学","北京航空大学"],
                "天通苑":["海底捞","呷脯呷脯","华联超市"]
            },
            "海淀":{
                "公主坟":["军事博物馆","中华世纪园"],
                "库普场馆":["中国科技馆","北京天文馆"],
                "高校":["北京大学","清华大学"],
                "景区":["北京植物园","香山公园","玉渊潭公园"]
            },
            "朝阳":{
                "龙城":["鸟化石国家地址公园","朝阳南北塔"],
                "双塔":["徜徉凌河公园","朝阳凤凰山"]
            },
            "延庆":{
                "龙庆峡":["龙庆峡景区"]
            }
        },
        "上海":{
            "宝山区":{
                "游玩":["顾村公园","上海玻璃博物馆","宝山净寺"],
                "美食":["海底捞火锅","宝山寺食堂","海上会","户外烧烤联盟"],
                "特色商圈":["万达广场","长江国际商业购物中心","上海罗店宝龙广场"]
            },
            "青浦区":{
                "游玩":["朱家角古镇","东方绿洲","上海大观园"],
                "美食":["函大隆酱园","江南第一茶楼","海鲜大排档"],
                "特色商圈":["国家会展中心商业广场","百联奥特莱斯","夏都小镇"],
            },
            "松江区":{
                "游玩":["上海欢乐谷","上海影视乐园","上海辰山植物园"],
                "美食":["榴芒无罪","盘古烤猪蹄","爱丽丝梦游仙境主题公司"],
                "特色商圈": ["没有"],
            },
            }
        }
    # 打印城市
    def print_place(choice):
        for i in choice:
            print(i)
    #攻略
    for i in data:
        print(i)
    while True:
        city1 = input("请输入您要去的城市：")
        if city1 in data:
            print_place(data[city1])
            city2 = input("请输入二级城市：")
            if city2 in data[city1]:
                print_place(data[city1][city2])
                city3 = input("请输入三级地区：")
                if city3 in data[city1][city2]:
                    print_place(data[city1][city2][city3])
                    user = input("是否要购物：y/n")
                    if user == "y":
                        shopping()
                    else:
                        print("确定不买点特产？")
                else:
                    print("您输入的三级地区不存在！请从新输入")
       
            else:
                print("您输入的二级城市不存在！请从新输入")
        else:
            print("您输入的城市不存在！请从新输入")
            break


print("---------------------------------------")
city_1 = print("===========1.旅游策略===============")
shopping_1 = print("===========2.购物商城===============")
print("---------------------------------------")
num = input("请选择您想要的：")
num = int(num)

while True:
    if num == 1:
        city()
        break
    elif num == 2:
        shopping()
        break
    else:
        print("输入有误，从新输入")
        break




















