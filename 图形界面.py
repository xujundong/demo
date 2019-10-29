# -*- coding: utf-8 -*-
# @Time    : 2019-01-11 14:19
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : 图形界面.py

from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self,text="hello world")
        self.helloLabel.pack()
        self.quitButton=Button(self,text="quit",command=self.quit)
        self.quitButton.pack()

app=Application()
app.master.title("hello world")
app.mainloop()