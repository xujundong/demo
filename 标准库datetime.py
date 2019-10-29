# -*- coding: utf-8 -*-
# @Time    : 2019-01-10 17:25
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : 标准库datetime.py
from datetime import datetime
#获取当前时间
now=datetime.now()
print(now)
#获取指定日期和时间
dt=datetime(2019,1,10,17,27,00)
print(dt)
#datetime转化为timestamp
ts=dt.timestamp()
print(ts)
#timestamp转化为datetime
dtt=datetime.fromtimestamp(ts)
print(dtt)
#str转换为datetime
str="2019-01-10 17:27:12"
day=datetime.strptime(str,"%Y-%m-%d %H:%M:%S")
print(day)
print(type(day))
#datetime转换为str
nowstr=now.strftime("%Y-%m-%d %H:%M:%S")
print(nowstr)
print(type(nowstr))