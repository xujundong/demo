# -*- coding: utf-8 -*-
# @Time    : 2019-01-10 17:16
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : test.py
import hashlib
def fun_md5(arg):
    hash=hashlib.md5()
    hash.update(arg.encode("utf-8"))
    m=hash.hexdigest()
    return m

f={"michael":"e10adc3949ba59abbe56e057f20f883e",
    "bob":"e10adc3949ba59abbe56e057f20f883e",
    "alice":"e10adc3949ba59abbe56e057f20f883e"}
def login(user1,pwd1):
        for a,b in f.items():
            if user1==a and fun_md5(pwd1)==b:
                return True



print(login("bob","123456"))
