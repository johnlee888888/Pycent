# -*- coding: utf-8 -*-
"""
Created on 2019/5/30 17:12

File name   文件遍历.py

@author: john lee
"""
import os

#
# os.mkdir('test')
# os.chdir('test')
# qyt1 = open('qytang1.txt', 'w')
# qyt1.write('test file\n')
# qyt1.write('this is qytang\n')
# qyt1.close()
# qyt2 = open('qytang2.txt', 'w')
# qyt2.write('test file\n')
# qyt2.write('qytang python\n')
# qyt2.close()
# qyt3 = open('qytang3.txt', 'w')
# qyt3.write('test file\n')
# qyt3.write('this is python\n')
# qyt3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')

# print(os.listdir(os.getcwd()))
print('文件中包含\'qytang\'关键字的文件为', end=" ")
for x in os.listdir(os.getcwd()):
    if os.path.isfile(x):
        # print(x + '   is File')
        for y in (open(x, 'r')):
            if 'qytang' in y:
                print(x)


# else:
#     print(x + '        is folder')

# if os.path.isfile(x):
#      #print(x + '   is File')
#      for y in (open(x, 'r')):
#          if  'qytang' in y:
#              print(y)


# for x in os.listdir(os.getcwd()):
#     if os.path.isfile(x):
#         # print(x + '   is File')
#         for y in (open(x, 'r')):
#             if 'qytang' in y:
#                 print('文件中包含\'qytang\'关键字的文件为')
#                 print(x.)
