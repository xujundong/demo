a,b,c,d = 20,2.1,True,4+6j

print(type(a),type(b),type(c),type(d))

#isinstance 和 type 的区别在于：
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
a=111
print(isinstance(a,int))


#---------------------------list -------------------#
listA = ['a',123,23123,23,'b','cd']
listB = [123,'xxxx']
print(listA)# 输出完整列表
print(listA[0]) # 输出列表第一个元素
print(listA[1:3])# 从第二个开始输出到第三个元素
print(listA[2:])# 输出从第三个元素开始的所有元素
print(listA*2)# 输出两次列表
print(listA+listB)# 连接列表


#与Python字符串不一样的是，列表中的元素是可以改变的：
listB[0]= 567
print(listB)
#1、List写在方括号之间，元素用逗号隔开。
#2、和字符串一样，list可以被索引和切片。
#3、List可以使用+操作符进行拼接。
#4、List中的元素是可以改变的。


#-------------------元祖--------------------------#
tupleA = ('abcd', 786 , 2.23, 'runoob', 70.2)
tupleB = (123, 'runoob')
print(tupleA) #输出完整元组
print(tupleA[0])  #输出元组的第一个元素
print(tupleA[1:3])# 输出从第二个元素开始到第三个元素
print(tupleA[2:])# 输出从第三个元素开始的所有元素
print(tupleB*2)# 输出两次元组
print(tupleA+tupleB)# 连接元组


#构造包含 0 个或 1 个元素的元组
tupleC = ()
tupleD = (12,)
print(tupleC)
print(tupleD)

#-----------------------------集合---------------------#
#可以使用大括号 { } 或者 set() 函数创建集合
setA = {'tom','jim','mary','tom','jack','rose'}
print(setA)
a=set('abc')
print(a)

if 'rose' in setA:
    print('yes')
else:
    print('no')

# set可以进行集合运算
aa=set('avasdasdasdaf')
bb=set('asagadasgasda')
print(aa - bb) # a 和 b 的差集
print(aa | bb)# a 和 b 的并集.
print(aa & bb)  # a 和 b 的交集
print(aa ^ bb)  # a 和 b 中不同时存在的元素




#----------------------字典---------------------#
dict ={}
dict['one'] = 1
dict[2] = 2
print(dict)

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print(dict['one'])# 输出键为 'one' 的值
print(dict[2])# 输出键为 2 的值
print(tinydict)# 输出完整的字典
print(tinydict.keys())# 输出所有键
print(tinydict.values())# 输出所有值
print(R'\n')