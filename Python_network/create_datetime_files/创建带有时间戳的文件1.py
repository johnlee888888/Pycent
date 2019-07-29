# -*- coding: utf-8 -*-
"""
Created on 2019/6/16 20:50

File name   创建带有时间戳的文件.py

@author: john lee
"""
import datetime

right_now = (datetime.datetime.now())
now_date = (right_now.strftime("%Y-%m-%d"))
now_time = (right_now.strftime("%H-%M-%S"))
print(now_date)
print(now_time)
files = open('save_fivedayago_time_{0}_{1}.txt'.format(str(now_date), str(now_time)), 'w')
files.write(str(datetime.datetime.now() - datetime.timedelta(days=5)))
files.close()
