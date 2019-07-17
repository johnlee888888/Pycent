# -*- coding: utf-8 -*-
"""
Created on 2019/5/30 21:58

File name   列表比较.py

@author: john lee
"""
list1 = ['aaa', 'bbb', 'ccc', '123', (4, 5), 2.01]
list2 = ['bbb', '333', '123', '3.14', 2.01, (4, 5)]

for x in list1:
    if x in list2:
        print(x, 'in list1 and list 2')
    else:
        print(x, 'only in list1')
