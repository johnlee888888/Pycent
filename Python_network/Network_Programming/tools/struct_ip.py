# -*- coding: utf-8 -*-
"""
Created on 2019/7/15 15:03

File name   struct_ip.py

@author: john lee
"""
from socket import inet_aton
import struct
import ipaddress

ip_list = ['172.16.12.123',
           '172.16.12.3',
           '172.16.12.234',
           '172.16.12.12',
           '172.16.12.23',
           ]


def sort_ip(ips):
    return sorted(ips, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
    # return sorted(ips, key=lambda ip: ipaddress.ip_address(ip))


if __name__ == '__main__':
    print(sort_ip(ip_list))
