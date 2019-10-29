# -*- coding: utf-8 -*-
# @Time    : 2019-01-14 13:15
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : 学前班课5作业.py

#写一个餐厅菜单显示程序，根据不同的菜系分成顶级菜单：湘菜、粤菜等
#根据肉食、蔬菜、特色菜分为二级菜单，根据每个选项里面的各个菜式分
# 为三级菜单，可以根据你输入的菜系、菜类、菜式可以选择进入各子菜单，查看菜式，也可以选择退出菜单。

menu={
    "湘菜":{
        "湘菜荤菜":{
            "湘菜荤菜1",
            "湘菜荤菜2",
            "湘菜荤菜3",
            "湘菜荤菜4"
        },
        "湘菜蔬菜":{
            "湘菜蔬菜1",
            "湘菜蔬菜2",
            "湘菜蔬菜3",
            "湘菜蔬菜4"
        },
    },
    "粤菜":{
        "粤菜荤菜":{
            "粤菜荤菜1",
            "粤菜荤菜2",
            "粤菜荤菜3",
            "粤菜荤菜4"
        },
        "粤菜蔬菜": {
            "粤菜蔬菜1",
            "粤菜蔬菜2",
            "粤菜蔬菜3",
            "粤菜蔬菜4"
        },
    }
}
for i in menu:
    print(i)
while True:
    print("===============菜单===============")
    for i in menu:
        print(i)
    ch=input("Q退出")
    if ch in menu:
        while True:
            for two in menu[ch]:
                print(two)
            ch2=input("Q退出，B返回上一层")
            if ch2 in menu[ch]:
                while True:
                    for three in menu[ch][ch2]:
                        print(three)
                    ch3=input("Q退出，B返回上一层")
                    if ch3 in menu[ch][ch2]:
                        while True:
                            for frou in menu[ch][ch2][ch3]:
                                print(frou)
                    elif ch3=="b"or ch3=="B":
                        pass
                    elif ch3=="q"or ch3=="Q":
                        False
                    else:
                        print("输入错误")
            elif ch2=="b"or ch2=="B":
                break
            elif ch2=="q"or ch2=="Q":
                exit()
            else:
                print("输入错误")
    elif ch=="q"or ch=="Q":
        exit()
    else:
        print("输入错误")