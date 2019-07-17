# -*- coding: utf-8 -*-
"""
Created on 2019/6/22 18:31

File name   正则表达式匹配2.py

@author: john lee
"""
import re

str1 = 'Port-channel1.189       192.168.189.254 Yes     CONFIG  up'


result = re.match('(\\s*\\w\\w\\w\\w.*\\d.\\w\\w\\w)\\s+(\\w{1,3}.'
                  '\\w{1,3}.\\w{1,3}.\\w{1,3})\\s+Yes\\s+CONFIG\\s+(\\w\\w)', str1).groups()

list2 = list(result)

line1 = '接口         :   {0: <9}' '\n' 'IP地址      :   {1: <5}' '\n' '状态         :   {2: <5}'\
    .format(list2[0], list2[1], list2[2])


length = len(line1)
print('=' * length)
print(line1)
print('=' * length)
