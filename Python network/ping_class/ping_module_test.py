# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 15:02

File name   ping.py

@author: john lee
"""
from kamene.all import *
import logging
import re

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def lee_ping(ip):
    ping_packet = IP(src='192.168.0.109', dst=ip) / ICMP()
    ping_result = sr1(ping_packet, timeout=2, verbose=False)
    print(ping_result)
    if ping_result:
        return '可达!'
    else:
        return '不通!'


if __name__ == '__main__':
    print(lee_ping('223.5.5.5'))
