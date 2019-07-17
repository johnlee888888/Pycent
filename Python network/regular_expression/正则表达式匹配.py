# -*- coding: utf-8 -*-
"""
Created on 2019/5/25 22:29

File name   正则表达式匹配.py

@author: john lee
"""
import re

str1 = '166  54a2.74f7.0326    DYNAMIC     Gi1/0/11'

result = re.match('(\s?\d\d\d\d?)\s+(\w\w\w\w.\w\w\w\w.\w\w\w\w)\s+(DYNAMIC|STATIC)\s+(.*/\d/\d\d)\s?',str1).groups()

a = (list(result))
b = ['VLAN ID', 'MAC', 'Type', 'Interface']
c = [':']
line1 = '{0: <10}{8: ^6}{1: ^10}\n{2: <12}{8: ^6}{3: ^20}\n{4: <13}{8: ^6}{5:^14}\n{6: <11}{8: ^6}{7: ^15}'\
    .format(b[0], a[0], b[1], a[1], b[2], a[2], b[3],  a[3], c[0])
length = (len(line1))
print('-' * length)
print(line1)






