# -*- coding: utf-8 -*-
"""
Created on 2019/7/17 14:51

File name   UDP_socket_client.py

@author: john lee
"""
import socket


address = ("192.168.107.128", 6666)
# 创建UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 收集客户输入信息
    msg = input('请输入数据:')
    # 如果客户输入为空发送空数据,并且退出
    if not msg:
        s.sendto(msg.encode(), address)
        break
    # 如果客户输入不为空,发送数据
    s.sendto(msg.encode(), address)

s.close()
