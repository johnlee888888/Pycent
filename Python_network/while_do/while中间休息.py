# -*- coding: utf-8 -*-
"""
Created on 2019/6/4 11:00

File name   while中间休息.py

@author: john lee
"""

import time

while True:
    try:
        time.sleep(2)
        print('ctrl + c to stop')
    except KeyboardInterrupt:
        print('按下了ctrl + c')
        print('退出程序')
        break
