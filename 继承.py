class Animal:
    def __init__(self,name,color):
        self.name=name
        self.__color=color
    def eat(self):
        print("吃的很开心")
    def __test(self):
        print("Animal私有父类方法")
    def test2(self):
        self.__test()
    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color
class Cat(Animal):
    def __init__(self,name,color,age):    #子类所有属性
        Animal.__init__(self,name,color)   #Cat继承Animal，init方法直接把父类的属性拿过来
        self.age=age                        #子类自己新增的属性
    def run(self):
        print("running")
A=Animal("aa","hongse")
A.test2()
A.setColor("heise")
print(A.getColor())
cat=Cat("haha","zise",12)
cat.eat()
cat.run()
#子类不能直接调用父类的私有属性
# cat.color
cat.setColor("huise")
print(cat.getColor())
cat.name="xixi"
cat.setColor("chengse")
cat.age=11
print(cat.name)
print(cat.getColor())
print(cat.age)
#子类不能直接用父类的私有方法，必须调父类的公用方法
# cat.__test()