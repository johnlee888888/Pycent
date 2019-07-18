# -*- coding: utf-8 -*-
"""
Created on 2019/7/17 14:27

File name   UDP_socket_server.py

@author: john lee
"""
import sys
from Get_ip_address import get_ip_addr
import socket

address = ("192.168.107.128", 6666)
# 创建UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 套接字绑定到IP地址
s.bind(address)

print('UDP服务器就绪!等待客户数据')
while True:
    try:
        # 接收UDP套接字的数据,2028为最大上限,不推荐接受大量数据
        aa = s.recvfrom(2048)
        data, addr = aa
        # 如果用户发来空数据就退出循环
        if not data:
            print('客户端退出!')
            break
        # 如果用户发来数据不是空的,就显示数据,与源信息
        print('接受到数据:', data, "来自于:", addr)
    except KeyboardInterrupt:
        sys.exit()
s.close()
