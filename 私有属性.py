class person:
    def __init__(self,name):
        self.__name=name

    #私有属性
    def setName(self,name):
        if len(name)>5:
            self.__name=name
        else:
            print("长度不符合要求")
    def getName(self):
        return self.__name

    #私有方法
    def __test(self):
        print("test")
    #调用私有方法
    def test2(self):
        self.__test()


p = person("xiao")
# print(p.getName())
p.setName("a")
print(p.getName())

p.test2()