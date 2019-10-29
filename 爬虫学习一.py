# -*- coding: utf-8 -*-
# @Time    : 2019-01-16 17:18
# @Author  : XuJundong
# @Email   : xujundong@nnuo.com
# @File    : 爬虫学习一.py


import request


url="https://www.jss.com.cn/"
# headers={"User-Agent":""}
page=request.get(url)
print(page)