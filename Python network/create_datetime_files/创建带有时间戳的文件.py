# -*- coding: utf-8 -*-
"""
Created on 2019/6/16 20:50

File name   创建带有时间戳的文件.py

@author: john lee
"""
import datetime
import os

fiveday = (datetime.datetime.now() + datetime.timedelta(days=5))
five_date = (fiveday.strftime("%Y-%m-%d"))
five_time = (fiveday.strftime("%H-%M-%S"))
print(five_date)
print(five_time)
files = open('save_fivedayago_time_{0}_{1}.txt'.format(str(five_date), str(five_time)), 'w')
files.write(str(datetime.datetime.now()))
files.close()

