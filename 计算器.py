# -*- coding: utf-8 -*-
# @Time    : 2019-01-11 15:03
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : 计算器.py


import re
import tkinter
import tkinter.messagebox

root=tkinter.Tk()
root.geometry("320x270+800+200")
root.resizable(False,False)
root.title("计算器")

xianshiqiVar=tkinter.StringVar(root,'')
xianshiqiEntry=tkinter.Entry(root,textvariable=xianshiqiVar)
xianshiqiEntry["state"]="readonly"
xianshiqiEntry.place(x=10,y=10,width=280,height=20)

def buttonClick(btn):
    content=xianshiqiVar.get()
    if content.startswith("."):
        content="0"+content
    elif btn==".":
        lastPart=re.split(r"\+|-|\*|/]",content)[-1]
        if "." in lastPart:
            tkinter.messagebox.showerror("错误","小数点太多了")
            return
        else:
            content+=btn
    elif btn=="C":
        content=""
    elif btn=="=":
        try:
            content=str(eval(content))
        except:
            tkinter.messagebox.showerror("错误","表达式错误")
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror("错误","不允许存在连续运算符")
            return
            content+=btn
        elif btn=="Sqrt":
            n=content.split(".")
            if all(map(lambda x:x.isdigit(),n)):
                content=eval(content)**0.5
            else:
                tkinter.messagebox.showerror("错误","表达式错误")
                return
    xianshiqiVar.set(content)


btnClear=tkinter.Button(root,text="Clear",command=lambda :buttonClick("C"))
btnClear.place(x=40,y=40,width=80,height=20)
btnCompute=tkinter.Button(root,text="=",command=lambda :buttonClick("="))
btnCompute.place(x=170,y=40,width=80,height=20)

digits=list("0123456789.")+["Sqrt"]
index=0
for row in range(4):
    for col in range(3):
        d=digits[index]
        index+=1
        btnDigit=tkinter.Button(root,text=d,command=lambda x=d:buttonClick(x))
        btnDigit.place(x=20+col*70,y=80+row*50,width=80,height=20)


operators=("+","-","*","/","**","//")
for index,operator in enumerate(operators):
    btnOperator=tkinter.Button(root,text=operator,command=lambda x=operator:buttonClick(x))
    btnOperator.place(x=230,y=80+index*30,width=50,height=20)



root.mainloop()

