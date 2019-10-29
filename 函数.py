def testprint():
    print("函数真简单")

#带形参
def add(a,b):
    c = a+b
    print(c)
def add2(a,b,c):
    d=a+b-c
    print(d)

#缺省参数，不传参数=默认值
def printinf(name,age=18):
    print(name,age)

#不定长参数,*args其实就是一个tuple元组,**kwargs其实就是一个字典
def functionname(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

#带有返回值的函数
def add4(a,b):
    return a+b

x=add4(11,22)
print(x)

#带多个返回值的函数
def return2(a,b):
    jia=a+b
    jian=a-b
    return jia,jian
testreturn1=return2(10,5)
print(testreturn1[1])

testprint()
add(1,2)
add2(1,2,3)
printinf("xujundong",321)
functionname(1,2,"sd","ad",m=1,n=2,c=123)

#递归函数，调用自身
def testdigui(n):
    if n==1:
        return 1
    return n*testdigui(n-1)

print(testdigui(10))


#匿名函数，用lambda申明
sum = lambda a,b:a+b
print(sum(2222,2))

#匿名函数的用途，函数作为参数传递
def testadd5(a,b,add):
    print(a)
    print(b)
    print("add:%d"%add(a,b))

testadd5(1,2,lambda a,b:a+b)

#作为内置函数的参数
stus = [ {"name":"zhangsan", "age":18}, {"name":"lisi", "age":19}, {"name":"wangwu", "age":17} ]
stus.sort(key= lambda x:x['name'])
print(stus)


