# -*- coding: utf-8 -*-
"""
Created on 2019/6/30 21:43

File name   ping_modules_new.py

@author: john lee
"""

from kamene.config import conf
conf.ipv6_enabled = False
from kamene.all import *
import logging


logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_packet = IP(dst=ip) / ICMP()
    ping_result = kamene.all.sr1(ping_packet, timeout=2, verbose=False)
    if ping_result:
        return '通!'
    else:
        return '不通!'


if __name__ == '__main__':
    result = qytang_ping('8.8.8.8')
    print('8.8.8.8', result)
