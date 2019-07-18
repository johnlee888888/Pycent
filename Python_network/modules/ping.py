# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 15:02

File name   ping.py

@author: john lee
"""
from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_packet = IP(dst=ip) / ICMP()
    ping_result = scapy.all.sr1(ping_packet, timeout=2, verbose=False)
    if ping_result:
        print(ip, '通')
        return '可达'
    else:
        print(ip, '不通')
        return '不通'


if __name__ == '__main__':
    result = qytang_ping('8.8.8.8')
    print(result)
