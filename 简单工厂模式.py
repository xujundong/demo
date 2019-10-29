class Person(object):
    def __init__(self,name):
        self.name=name

    def work(self,type):
        print("%s开始工作了"%self.name)
        a=Factory.create(type)
        a.kanshu()

class Axe(object):
    def __init__(self,name):
        self.name=name

    def kanshu(self):
        print("正在砍树")

class futou(Axe):
    def kanshu(self):
        print("用斧头砍树")

class gangju(Axe):
    def kanshu(self):
        print("用钢锯砍树")

#工长类
class Factory(object):
    @staticmethod
    def create(type):
        if type=="futou":
            return futou("斧头")
        elif type=="gangju":
            return gangju("钢锯")
        else:
            print("输入错误")


p=Person("张三")
p.work("gangju")