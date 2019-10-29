#申明字典dict
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"a","b","c"} #其实就是一个set
#多层字典，for循环打印在外面的一层keys
dict4={"s":{"ss"},
       "z":{"zz"}}
print(type(dict4))
for i in dict4:
    print(i)
#打印字段
print(dict1)
print(dict2)

#修改元素
dict1["a"]=111111
print(dict1)
newa = input("输入新的值")
dict1["d"]=int(newa)
print(dict1)

#添加元素
newid = input("输入新的值")
dict1["id"]=newid
print(dict1)

#删除元素del clear()
#del删除指定的元素
del dict1["a"]
print(dict1)
# del dict1#删除整个字典
#clear 清除整个字典
# dict1.clear()
print(dict1) #打印失败，dict1被清除了

#字典常见函数
#len()测量字典中，键值对的个数
print(len(dict1))
#keys返回一个包含字典所有KEY的列表
print(dict1.keys())
#values 返回一个包含字典所有value的列表
print(dict1.values())
#items返回一个包含字典所有value的列表
print(dict1.items())


#字典遍历
#遍历字典的key（键）
for key in dict1.keys():
    print(key)
#遍历字典的value（值）
for value in dict1.values():
    print(value)
#遍历字典的项（元素）
for item in dict1.items():
    print(item)
#遍历字典的key-value（键值对）
for key,value in dict1.items():
    print(key,value)




#...1、可变类型，值可以改变：
# 列表 list
# 字典 dict
# set  （没有value的字典）
# 2、不可变类型，值不可以改变：
# 数值类型 int, long, bool, float
# 字符串 str
# 元组 tuple