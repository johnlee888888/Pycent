# -*- coding: utf-8 -*-
"""
Created on 2019/6/27 10:11

File name   字典2.py

@author: john lee
"""
import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n" \
           " TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
find_key = asa_conn.split('\n')


k3 = {}

for info in find_key:
    k1 = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)', info).groups()
    v1 = re.match(r'.*\s+(\w+),\s+\w+\s+(\w+)', info).groups()
    if k1 and v1:
        k3[k1] = v1

print('\n打印字典\n', k3)
list1 = []
for x in k3:
    if x:
        list1.append(x)
        print(list1)

# 正则匹配key1
# k1 = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)\s+\w+\s+'
#               r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)', str1[0]).groups()
# # 正则匹配values1
# v1 = re.match(r'.*\s+(\w+),\s+\w+\s+(\w+)', str1[0]).groups()
# # 正则匹配key2
# k2 = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)\s+\w+\s+'
#               r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)', str1[1]).groups()
# # 正则匹配values2
# v2 = re.match(r'.*\s+(\w+),\s+\w+\s+(\w+)', str1[1]).groups()
# # 产生字典
# dict_1 = {k2: v2, k1: v1}

#
# line1 = '   src : {0:<6}   |   src_p : {1:<10}|    dst : {2:<6}|   dst_p : {3:<10}| '.format(k3.keys(), k1[1], k1[2], k1[3])
# line2 = ' bytes : {0:<18}|   flags : {1:<10}'.format(v1[0], v1[1])
# line3 = '   src : {0:<6}   |   src_p : {1:<10}|    dst : {2:<6}|   dst_p : {3:<10}| '.format(k1[0], k1[1], k1[2], k1[3])
# line4 = ' bytes : {0:<18}|   flags : {1:<10}'.format(v1[0], v1[1])
#
# length = len(line1)
# print('\n格式化打印输出\n')
# print(line1)
# print(line2)
# print('=' * length)
# print(line3)
# print(line4)
# print('=' * length)
