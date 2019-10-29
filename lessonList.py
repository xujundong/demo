list1 = ['aaa','bbb','cccc','dddd']
list2 = [1,2,3,4]
print(list1[0])
print(list2[0:4])
list1[0] = 'eee'
print(list1)

print(list1)


print(len(list1)) #列表元素个数
print(max(list1)) #返回列表元素最大值
print(min(list1)) #返回列表元素最小值
#print(list1(seq)) #将元组转换为列表
list1.append('xxx')
print(list1)
print(list1.count('xxx'))
