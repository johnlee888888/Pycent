# -*- coding: utf-8 -*-
"""
Created on 2019/5/14 18:07

File name   base.py

@author: john lee
"""
res = [c * 4 for c in 'qytang']
print(res)

testlist = []
for c in 'qytang':
    testlist.append(c * 4)
print(testlist)


l1 = [1,2,4,5,23,314,323,3,2,1,4,1]
l2= set(l1)
print(l2)