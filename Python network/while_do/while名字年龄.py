# -*- coding: utf-8 -*-
"""
Created on 2019/6/4 11:28

File name   while名字年龄.py

@author: john lee
"""

while True:
    name = input('please input your name !')
    if name == 'stop': break
    age = input('please input your age !')
    print('hello !', name,'=>',int(age)**2)