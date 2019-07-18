# -*- coding: utf-8 -*-
"""
Created on 2019/7/1 17:27

File name   while监听端口.py

@author: john lee
"""
import time
import os
import re


while True:
    port = os.popen('netstat ' + '-tulnp').read()
    if re.findall(r'\s+\w\w\w\s+.*\d+\s+\d+\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:80', port):
        print('80端口已经打开!')
        time.sleep(2)
    else:
        print('等待2秒再监控')
        time.sleep(2)
