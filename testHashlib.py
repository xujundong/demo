# -*- coding: utf-8 -*-
# @Time    : 2019-01-11 10:36
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : testHashlib.py

import hashlib
# md5=hashlib.md5()
# md5.update("123456".encode("utf-8"))
# print(md5.hexdigest())

def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()

# print(calc_md5("123456"))

db={"michael":"e10adc3949ba59abbe56e057f20f883e",
    "bob":"e10adc3949ba59abbe56e057f20f883e",
    "alice":"e10adc3949ba59abbe56e057f20f883e"}
print(len(db))
def login(user,password):
    pd=calc_md5(password)
    for u,p in db.items():
        print(u,p)
#
# #
print(login("bob","123456"))