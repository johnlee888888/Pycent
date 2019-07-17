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
    try:
        port = os.popen('netstat ' + '-tulnp').read()
        if re.findall(r'\s+(tcp|udp)\s+.*\d+\s+\d+\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:80', port):
            print('80端口已经打开!')
            time.sleep(2)
        else:
            print('等待2秒再监控端口!')
            time.sleep(2)
    except KeyboardInterrupt:
        print('收到停止命令,请稍后!')
        time.sleep(1)
        print('退出程序')
        break
