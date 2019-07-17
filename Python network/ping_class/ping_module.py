# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 15:02

File name   ping.py

@author: john lee
"""
from kamene.all import *
import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def lee_ping(ip):
    ping_packet = IP(dst=ip) / ICMP()
    ping_result = kamene.all.sr1(ping_packet, timeout=2, verbose=False)
    if ping_result:
        return '可达!'
    else:
        return '不通!'


if __name__ == '__main__':
    print(lee_ping('192.168.0.1')*5, )
