# -*- coding: utf-8 -*-
"""
Created on 2019/5/18 14:00

File name   复制列表.py

@author: john lee
"""
l1 = [4, 5, 7, 1, 3, 9, 0]

l2 = l1.copy()

l2.sort()

for i in range(len(l1)):
    print(l1[i], l2[i])
