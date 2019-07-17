# -*- coding: utf-8 -*-
"""
Created on 2019/6/4 15:02

File name   函数比较.py

@author: john lee
"""

str1 = 'Stacking'
str2 = 'Staking'


def find_same(x, y):
    same_list = []
    for a in x:
        if a in y:
            same_list.append(a)
    return same_list


print(find_same(str1, str2))
