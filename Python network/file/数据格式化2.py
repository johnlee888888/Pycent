# -*- coding: utf-8 -*-
"""
Created on 2019/5/22 21:15

File name   数据格式化2.py

@author: john lee
"""
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_Fees_SEC = 456789.12456
COURSE_Fees_Python = 1234.3456

line1 = "Department1    name:{0: <10}Manager:{1: <10}COURSE_FEES:{2:<10.2f} \
    The End!".format(department1, depart1_m, COURSE_Fees_SEC)
line2 = "Department2    name:{0: <10}Manager:{1: <15}COURSE_FEES:{2:<10.2f}  \
    The End!".format(department2, depart2_m, COURSE_Fees_Python)


length = len(line1)
print('=' * length)
print(line1)
print(line2)
print('=' * length)