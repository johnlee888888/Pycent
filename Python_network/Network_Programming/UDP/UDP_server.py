# -*- coding: utf-8 -*-
"""
Created on 2019/7/17 10:50

File name   UDP_server.py

@author: john lee
"""
import socket
import pickle
import sys
import hashlib


def udp_server(ip, port):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('UDP服务器就绪! 等待客户数据')
    while True:
        try:
            # 接受UDP套接字的数据,2048为接受的最大数量,多的直接丢弃!
            # 不推荐使用UDP传大量数据
            recv_source_data = s.recvfrom(2048)
            s.bind(address)
            data, addr = recv_source_data
            if not data:
                print('客户端退出!')
                break

            if md5_recv == md5_value.encode():
                print('=' * 80)
                print("{0:<30}:{1:<30}".format("数据来自于", str(addr)))
                print("{0:<30}:{1:<30}".format("数据序号为", seq_id))
                print("{0:<30}:{1:<30}".format("数据长度为", length))
                print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))

        except KeyboardInterrupt:
            sys.exit()

