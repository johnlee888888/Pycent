# -*- coding: utf-8 -*-
"""
Created on 2019/6/27 21:51

File name   字典3.py

@author: john lee
"""
import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n" \
           " TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
find_key = asa_conn.split('\n')


asa_dict = {}

for info in find_key:
    k1 = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
                  r':(\d+).*\s+(\w+),\s+\w+\s+(\w+)', info).groups()
    asa_dict[(k1[0]), (k1[1]), (k1[2]), (k1[3])] = ((k1[4]), (k1[5]))
print('打印分析后的字典!\n')
print(asa_dict)


format_str1 = '   src : {0:<6}   |   src_p : {1:^10}|    dst : {2:<6}    |   dst_p : {3:<10}| '
format_str2 = ' bytes : {0:^15}   |   flags : {1:^10}'

print('\n格式化打印输出\n')
for key, values in asa_dict.items():
    line1 = format_str1.format(key[0], key[1], key[2], key[3])
    line2 = format_str2.format(values[0], values[1])
    length = len(line1)
    print(line1)
    print(line2)
    print('=' * length)
