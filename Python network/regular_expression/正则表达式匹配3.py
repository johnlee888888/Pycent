# -*- coding: utf-8 -*-
"""
Created on 2019/6/24 10:42

File name   正则表达式匹配3.py

@author: john lee
"""
import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

line1 = re.match('\s*(\w\w\w)\s+.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})\s+.*\s+'
                 '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}),\s+.*\s+(\w\w?):(\w\w):(\w\w),\s+'
                 '.*\s+(\d\d\d\d\d\d\d\d),\s+.*(\w\w\w)', str1).groups()

a1 = list(line1)

b1 = 'protocol            :     {0: <5}\nserver               :     {1: <5}\n' \
     'localserver       :     {2: <5}\nidle                   :     {3: <1}' \
     ' 小时 {4: <1}分钟 {5: <1}秒\nbytes                :     {6: <5}\n' \
     'flags                 :     {7: <5}'\
    .format(a1[0], a1[1], a1[2], a1[3], a1[4], a1[5], a1[6], a1[7])
print(b1)

