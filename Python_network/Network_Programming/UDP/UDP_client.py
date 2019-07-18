# -*- coding: utf-8 -*-
"""
Created on 2019/7/17 10:50

File name   UDP_client.py

@author: john lee
"""
import socket
import pickle
import hashlib
import struct

m = hashlib.md5()


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        send_data = pickle.dumps(x)
        header = struct.pack('!hhii', version, pkt_type, seq_id, len(x))
        m.update(x.encode())
        md5 = m.hexdigest()
        print(md5)
        md5_value = struct.pack('!16c', b'md5')
        print(header)
        print(md5_value)
        # print(send_data)
        # m.update(str(data_list).encode())
        # check = m.hexdigest()
        # print(check)
        s.sendto(header, address)
        seq_id += 1
        # print(seq_id)
    s.close()


if __name__ == '__main__':
    user_data = ['qytang', [1, 'qyt', 3], {'qytang': 1, 'test': 3}]
    udp_send_data('192.168.107.128', 6666, user_data)
