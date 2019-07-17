# -*- coding: utf-8 -*-
"""
Created on 2019/5/26 19:06

File name   字典.py

@author: john lee
"""

import re

str1 = 'TCP student 192.168.189.167:32806 Teacher 137.78.5.128:65247,idle 0:00:00, bytes 74,flags UIO'
str2 = 'TCP student 192.168.189.167:80 Teacher 137.78.5.128:65233,idle 0:00:03,bytes 334516,flags UIO'

# line1
source_ip1 = re.match('TCP\\s+student\\s+(\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3})', str1).groups()
source_port1 = re.match('TCP\\s+student\\s+192.168.189.167:(\\d{1,5})', str1).groups()
destination_ip1 = re.match('TCP\\s+student\\s+192.168.189.167:32806\\s+Teacher\
\\s+(\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3})', str1).groups()
destination_port1 = re.match('TCP\\s+student\\s+192.168.189.167:32806\\s+Teacher\
\\s+137.78.5.128:(\\d{1,5})', str1).groups()
byte1 = re.match('TCP\\s+student\\s+192.168.189.167:32806\\s+Teacher\
\\s+137.78.5.128:65247\\s*,idle\\s0:00:00,\\s+bytes\\s+(\\d{1,2})', str1).groups()
flag1 = re.match('TCP\\s+student\\s+192.168.189.167:32806\\s+Teacher\
\\s+137.78.5.128:65247\\s*,idle\\s0:00:00,\\s+bytes\\s+74,flags\\s+(\\w{1,3})', str1).groups()

# line2
source_ip2 = re.match('TCP\\s+student\\s+(\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3})', str2).groups()
source_port2 = re.match('TCP\\s+student\\s+192.168.189.167:(\\d{1,2})', str2).groups()
destination_ip2 = re.match('TCP\\s+student\\s+192.168.189.167:80\\s+Teacher\
\\s+(\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3})', str2).groups()
destination_port2 = (re.match('TCP\\s+student\\s+192.168.189.167:80\\s+Teacher\
\\s+137.78.5.128:(\\d{1,5})', str2).groups())
byte2 = (re.match('TCP\\s+student\\s+192.168.189.167:80\\s+Teacher\
\\s+137.78.5.128:65233,idle\\s+0:00:03,bytes\\s+(\\d{1,6})', str2).groups())
flag2 = re.match('TCP\\s+student\\s+192.168.189.167:80\\s+Teacher\
\\s+137.78.5.128:65233,idle\\s+0:00:03,bytes\\s+334516,flags\\s+(\\w{1,3})', str2).groups()

a_1 = (source_ip1 + source_port1 + destination_ip1 + destination_port1)
a_2 = (byte1 + flag1)
a_dict = {(a_1): (a_2)}

b_1 = (source_ip2 + source_port2 + destination_ip2 + destination_port2)
b_2 = (byte2 + flag2)
b_dict = {(b_1): (b_2)}

a_dict.update(b_dict)

s_ip = str(source_ip1)
s_p = str(source_port1)
d_ip = str(destination_ip1)
d_p = str(destination_port1)
by = str(byte1)
fl = str(flag1)

s_ip2 = str(source_ip2)
s_p2 = str(source_port2)
d_ip2 = str(destination_ip2)
d_p2 = str(destination_port2)
by2 = str(byte2)
fl2 = str(flag2)

f1 = 'src  : {0: <10}          |           src_p   :   {1:<10}         |           dst    :    {2:<10}       |   dst_p:   {3:<10} \n' \
     ' bytes    :   {4:<10}                     |           flags :     {5:<10}'. \
    format(s_ip, s_p, d_ip, d_p, by, fl)
f2 = 'src  : {0: <10}          |           src_p   :   {1:<10}            |           dst    :    {2:<10}       |   dst_p:   {3:<10} \n' \
     ' bytes    :   {4:<10}                |           flags :     {5:<10}'. \
    format(s_ip2, s_p2, d_ip2, d_p2, by2, fl2)
length = len(f1)
print('打印字典')
print(a_dict)
print(' ' * length)
print(' ' * length)
print('格式化打印输出')
print(f1)
print('=' * length)
print(f2)
print('=' * length)
