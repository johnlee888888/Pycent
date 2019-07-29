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
import struct

m = hashlib.md5()
address = ('192.168.107.1', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
print('UDP服务器就绪! 等待客户数据')
while True:
    try:
        # 接受UDP套接字的数据,2048为接受的最大数量,多的直接丢弃!
        # 不推荐使用UDP传大量数据
        recv_source_data = s.recvfrom(2048)
        data, addr = recv_source_data
        if not data:
            print('客户端退出!')
            break
        # 将收到的数据解包
        data_recv = (struct.unpack('40s12s32s', data)[0])
        # 将收到的header解包
        head = struct.unpack('40s12s32s', data)[1]
        header = struct.unpack('!hhii', head)
        # 分解出header中的序号和长度
        seq_id = header[2]
        length = header[3]
        # 将收到的MD5解包
        md5_recv = struct.unpack('40s12s32s', data)[2]
        # 将收到的数据进行MD5计算
        m.update(str(pickle.loads(data_recv)).encode())
        md5_value = m.hexdigest()
        # print(md5_value.encode())

        if md5_recv == md5_value.encode():
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据来自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序号为", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data_recv))))

    except KeyboardInterrupt:
        sys.exit()
s.close()
