class Car:
    def getInfo(self):
        print("info")

    def move(self):
        print("move")
    ##已经创建了对象，初始化对象回调方法
    def __init__(self,color,weelNum):
        print("init")
        self.color=color
        self.weelNum=weelNum
    #对象创建的回调方法
    def __new__(cls,weelNum,color):
        print("new")
        return object.__new__(cls)
    #和toString
    def __str__(self):
        return "%s---%s"%(self.color,self.weelNum)

    #对象回收时候回调
    def __del__(self):
        print("del%s"%self.weelNum)
BMW = Car("sss","黑色")
print(id(BMW))
print(BMW.color)
print(BMW.weelNum)
print(BMW)

print(id(BMW))