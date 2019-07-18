# -*- coding: utf-8 -*-
"""
Created on 2019/6/16 15:09

File name   sys_test.py

@author: john lee
"""
import sys


if 'win32' in sys.platform:
    print( '这是windows环境')

elif 'linux' in sys.platform:
    print('这是linux环境')

else:
    print('这是其他系统')
