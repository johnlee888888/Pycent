# -*- coding: utf-8 -*-
"""
Created on 2019/6/27 22:42

File name   接口排序.py

@author: john lee
"""
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
a = sorted(port_list, key=lambda x: int(x.split('/')[3])+(int(x.split('/')[2])*100))
print(a)


# sorted(port_list, key=lambda x: int(x[0].split('/')[3])+(int(a.split('/')*100)))