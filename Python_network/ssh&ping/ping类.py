# -*- coding: utf-8 -*-
"""
Created on 2019/6/16 13:08

File name   ping类.py

@author: john lee
"""

from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_packet = IP(dst=ip) / ICMP()
    ping_result = scapy.all.sr1(ping_packet, timeout=2, verbose=False)
    if ping_result:
        return '可达'
    else:
        return '不通'


class Lee_ping:
    def __init__(self, ip):
        self.srcip = sip
        qytang_ping(ip)

    def src(self, sip):
        pass

    def size(self, length):
        self.len = length

    def one(self):
        self.pingip
