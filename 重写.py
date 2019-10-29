#重写，子类继承父类，方法名字一样，但重写过了，调用父类的方法，一共3种方式
class Cat():
    def info(self):
        print("cat . info ")

class bosi(Cat):
    def info(self):
        #第一种调用方式
        Cat.info(self)
        # 第二种调用方式
        super(bosi, self).info()
        # 第三种调用方式
        super().info()

b=bosi()
b.info()