class A():
    def test(self):
        print("A")

class B():
    def test(self):
        print("B")

class C(A,B):
    pass


c=C()
#mro()方法打印出对象搜索方法的先后顺序
print(C.mro())


class D(A,B):
    def test(self):
        A.test(self)

d=D()
d.test()

