# -*- coding: utf-8 -*-
"""
Created on 2019/5/30 17:12

File name   文件遍历.py

@author: john lee
"""
import os


os.mkdir('test1')
os.chdir('test1')
qyt1 = open('qytang1.txt', 'w')
qyt1.write('test file\n')
qyt1.write('this is qytang\n')
qyt1.close()
qyt2 = open('qytang2.txt', 'w')
qyt2.write('test file\n')
qyt2.write('qytang python\n')
qyt2.close()
qyt3 = open('qytang3.txt', 'w')
qyt3.write('test file\n')
qyt3.write('this is python\n')
qyt3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

print('文件中包含\'qytang\'关键字的文件为:')
print('方案一:')
for x in os.listdir(os.getcwd()):
    if os.path.isfile(x):
        for y in (open(x, 'r')):
            if 'qytang' in y:
                print('    ', x)

print('方案二:')
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for x in files:
        for y in (open(x, 'r')):
            if 'qytang' in y:
                print('    ', x)

# 执行清理
os.chdir('..')
for root, dirs, files in os.walk('test1', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('test1')
