# -*- coding: utf-8 -*-
"""
Created on 2019/6/4 17:19

File name   ping ip地址.py

@author: john lee
"""
from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

ping_pkt = IP(dst='192.168.0.1') / ICMP()
ping_result = scapy.all.sr1(ping_pkt, timeout=2, verbose=False)
ping_result.show()

print(ping_result)
