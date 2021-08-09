file = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")


list = []
for da in range(32):
    data = file.readline()
    li = data.split(" ",1)
    # print(li)
    list.append(li[0])


#统计操作
for index,value in enumerate(list):
    if value in list [:index]:
        continue
    else:
        print(value,"出现",list.count(value),"次!")