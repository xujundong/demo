class Person:
    #类方法，加@classmethod，形参cls
    @classmethod
    def test(cls):
        print("test")
    #静态方法，加@staticmethod，没有形参
    @staticmethod
    def test2():
        print("test2")
    #普通方法，def 方法名，形参self
    def test3(self):
        print("test3")

p=Person()
p.test()
p.test2()
p.test3()


