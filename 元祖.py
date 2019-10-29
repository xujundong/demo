#申明元祖
#元祖不可修改哦
tuple1=("a","b","c","d")
tuple2=(1,) #只有一个元素的时候要加上,
#打印
print(tuple1)

#通过列表list实现修改元祖
tuple3=("a","b",["c","d"])
tuple3[2][0]="C"
tuple3[2][1]="D"
print(tuple3)

#访问元祖，通过下标
print(tuple3[0])
print(tuple3[2][1])

#元组的内置函数count, index
#index 返回该元素的下标 注意是左闭右开区间
print(tuple3.index("b"))
#count 出现次数
print(tuple3.count("a"))