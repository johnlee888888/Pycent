# -*- coding: utf-8 -*-
"""
Created on 2019/6/22 18:04

File name   数据格式化3.py

@author: john lee
"""
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_Fees_SEC = 456789.12456
COURSE_Fees_Python = 1234.3456


# line1 = 'Department1 name:%-12sManager:%-15sCOURSE FEES:%-15.2f The End!' % (department1,
#                                                                              depart1_m, COURSE_Fees_SEC)
# line2 = 'Department2 name:%-12sManager:%-19sCOURSE FEES:%-17.2f The End!' % (department2,
#                                                                              depart2_m, COURSE_Fees_Python)

line1 = 'Department1    name:{0: <13}Manager:{1:<15}COURSE FEES:{2:<16.2f}The End!'.format(department1, depart1_m,
                                                                                           COURSE_Fees_SEC)
line2 = 'Department2    name:{0: <13}Manager:{1:<19}COURSE FEES:{2:<18.2f}The End!'.format(department2, depart2_m,
                                                                                           COURSE_Fees_Python)
length = len(line1)
print('=' * length)
print(line1)
print(line2)
print('=' * length)
