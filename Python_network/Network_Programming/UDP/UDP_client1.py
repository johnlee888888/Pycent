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
        header = struct.pack('!hhii', version, pkt_type, seq_id, len(send_data))
        m.update(str(x).encode())
        check = m.hexdigest()
        md5 = check.encode()

        s.sendto(struct.pack('40s12s32s', send_data, header, md5), address)

        seq_id += 1
    s.close()


if __name__ == '__main__':
    user_data = ['哈哈哈', [1, 'hello', 3], {'handsome': 1, 'test': 3}]
    udp_send_data('192.168.107.1', 6666, user_data)
