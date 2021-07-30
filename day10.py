class cup:
    __high = ""
    __volume = ""
    __colour = ""
    __quality = ""
    __liquid = ""
    def sethigh(self,high):
        self.__high = high

    def gethigh(self,high):
        return self.__high

    def setvolume(self, volume):
        self.__volume = volume

    def getvolume(self, volume):
        return self.__volume

    def setcolour(self, colour):
        self.__colour = colour

    def getcolour(self, colour):
        return self.__colour

    def setquality(self, quality):
        self.__quality = quality

    def getquality(self, quality):
        return self.__quality

    def setliquid(self, liquid):
        self.__liquid = liquid

    def getliquid(self, liquid):
        return self.__liquid

    def gaodu(self,high):
        print(self.__high,"高度是：",high)
    def rongji(self,volume):
        print(self.__volume,"可以装",volume,"升水")
    def yanse(self,colour):
        print(self.__colour,colour,"杯子的颜色是",colour)
    def caizhi(self,quality):
        print(self.__quality,quality,"材质是：",quality)
    def yeti(self,liquid):
        print(self.__liquid,"能存放的液体:",liquid)

g = cup()

g.gaodu("20")
g.rongji("750")
g.yanse("灰色")
g.caizhi("塑料")
g.yeti("可乐,雪碧")

print()

class computer():
    __username = ""
    __typing = ""
    __games = ""
    __videos = ""
    def settyping(self,typing):
        self.__typing = typing
    def gettyping(self):
        return self.__typing

    def setgames(self,games):
        self.__games = games
    def getgames(self):
        return self.__games

    def setvideos(self,videos):
        self.__videos = videos
    def getvideos(self):
        return self.__videos

    def setusername(self,username):
        self.__username = username
    def getusername(self):
        return self.__username

    def dazi(self,typing):
        print(self.__username,"正在",typing)

    def youxi(self,games):
        print(self.__username,"正在",games)

    def shipin(self,videos):
        print(self.__username,"正在",videos)

    def pingmu(self,screen):
        print("屏幕大小是：",screen)

    def jiage(self,price):
        print("价格是：",price)

    def cpu(self,cpu):
        print("cpu型号：",cpu)

    def neicun(self,memory):
        print("内存大小：",memory)

    def daiji(self,standby):
        print("屏幕大小是：",standby)

    def showme(self):
        print("我叫",self.__username,",","我在玩",self.__typing,",","我在",self.__games,",","我在看",self.__videos)

c = computer()
c.setusername("王锐")
c.settyping("红豆罗")
c.setgames("打字")
c.setvideos("速度与激情")
c.showme()

c.pingmu("759*1200")
c.jiage("50000")
c.cpu("40")
c.neicun("680")
c.daiji("200分")



