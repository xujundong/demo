#小明的成绩从去年的72分提升到了今年的85分，请计算小明
# 成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只
# 保留小数点后1位：

# print("小明成绩提示了%.1f%%"%(85-72))

#输出
# a = input()
# print(a)
# 由用输入一个学生的信息，（姓名，年龄，地址）。然后看看年龄是否是偶数，然后输出。
# print("请输入姓名")
# name = input()
# print("请输入年龄")
# age= input()
# print("请输入地址")
# add=input()
# if(int(age)%2==0):
#     print(name,age,add)

#1、要求：从键盘输入刀子的长度，如果刀子长度没有超过10cm，则允许上火车，否则不允许上火车
# changdu = input()
# if int(changdu)<10:
#     print("允许上火车")
# else:
#     print("不允许上火车")

#2、小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
# print("输入身高")
# shengao=input()
# print("输入体重")
# tizhong=input()
# shengao=float(shengao)
# tizhong=float(tizhong)
# BMI=tizhong/(shengao*shengao)
# print("BMI指数%.1f"%BMI)
# if BMI<18.5:
#     print("过轻")
# elif 18.5<=BMI<=25:
#     print("正常")
# elif 25<BMI<28:
#     print("过重")
# elif 28<BMI<32:
#     print("肥胖")
# elif BMI>32:
#     print("严重肥胖")


#3、情节描述：上公交车，并且可以有座位坐下
# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果空座位的数量大于0，就可以坐下

yue = input("输入公交卡当前的余额")
yue=int(yue)

if yue>=2:
    print("可以上公交")
    zuowei = input("输入公交车还有几个位置")
    zuowei = int(zuowei)
    if zuowei>0:
        print("有位置")
    else:
        print("没有位置")
else:
    print("不能上公交车")
