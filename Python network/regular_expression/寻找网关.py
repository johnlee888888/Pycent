# -*- coding: utf-8 -*-
"""
Created on 2019/5/30 14:51

File name   寻找网关.py

@author: john lee
"""
import re

route = open(r'C:\Users\ydboo\OneDrive\文档\Python network\route.txt', 'r')
r1 = route.readline()
gw = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+UG', r1).groups()
print('网关为:', gw[0])
