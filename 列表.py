#申明列表
list1 = ["a","b","c",1,2,3]

#打印列表
print(list1)

#通过索引获取元素,0开始，-1末尾
print(list1[0]) # a

#添加元素("增"append, extend, insert)
#append增加元素
list1.append("A")
print(list1)
#extend列表A增加到列表B
list2 = ["aa","bb"]
list1.extend(list2)
print(list1)
#insert在指定位置index前插入元素object----注意是前面
list1.insert(2,"AA")
print(list1)

#修改元素，直接通过索引= 什么来修改
list1[0]="XXX"
print(list1)

#查找元素 in not in 返回True False
print("a" in list1)
print("a" not in list1)

#index, count 索引和出现的次数 ，注意左闭右开区间
print(list1.index("XXX"))
print(list1.count("XXX"))

#删除元素("删"del, pop, remove)
#del 全部删除
del list2
# print(list2)
#pop默认删除最后一个元素,给指定的下标删除指定的元素
list1.pop()
print(list1)
list1.pop(2)
print(list1)
#remove 根据元素的值进行删除第一个
list1.remove("XXX")
print(list1)

#排序(sort, reverse)
#sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
a=[5,2,1,3,4]
a.sort()
print(a)
#reverse逆序排
a.reverse()
print(a)
#enumerate打印出下标，不常用
for i,chr in enumerate(list1):
    print(i,chr)
