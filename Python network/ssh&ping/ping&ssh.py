# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 22:31

File name   ping&ssh.py

@author: john lee
"""
from ping_module import qytang_ping
from ssh_connect import qytang_ssh


ip = '192.168.1.107'
result = qytang_ping(ip)
print(result)
if "可达"in result:
    print(ip, '可达')
    print('登录', ip, '执行命令 ls 的回显结果如下:')
    print(qytang_ssh(ip, 'john', 'cisc0123!', cmd='ls'))
else:
    print(ip, '不可达')

ip2 = '192.168.1.111'
result1 = qytang_ping(ip2)
if "可达"in result1:
    print(ip2, '可达')
    print('登录', ip2, '执行命令 ls 的回显结果如下:')
    print(qytang_ssh(ip2, 'john', 'cisc0123!', cmd='ls'))
else:
    print(ip2, '不可达')