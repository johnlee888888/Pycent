# -*- coding: utf-8 -*-
"""
Created on 2019/6/25 9:19

File name   匹配ens33.py

@author: john lee
"""
import os
import re
import random

ifconfig_result = 'ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n' \
                  '        inet 172.20.10.13  netmask 255.255.255.240  broadcast 172.20.10.15\n' \
                  '        inet6 fe80::d6b:6b44:4156:d89b  prefixlen 64  scopeid 0x20<link>\n' \
                  '        ether 00:0c:29:d4:06:18  txqueuelen 1000  (Ethernet)\n' \
                  '        RX packets 88687  bytes 130187197 (124.1 MiB)\n' \
                  '        RX errors 0  dropped 0  overruns 0  frame 0\n' \
                  '        TX packets 16152  bytes 1191366 (1.1 MiB)\n' \
                  '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'


# 正则表达式查找ip, 掩码, 广播和mac地址
ipv4_add = re.findall(r'inet\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ifconfig_result)[0]
netmask = re.findall(r'netmask\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ifconfig_result)[0]
mac_addr = re.findall(r'ether\s+(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)', ifconfig_result)[0]

# 格式化字符串
format_str = '{0:s} {1:s}'


# 打印结果
print(format_str.format('{0: <10}{1: >5}'.format('ipv4_add', ':'), ipv4_add))
print(format_str.format('{0: <10}{1: >5}'.format('netmask', ':'), netmask))
print(format_str.format('{0: <10}{1: >5}'.format('broadcast', ':'), broadcast))
print(format_str.format('{0: <10}{1: >5}'.format('mac_addr', ':'), mac_addr))

# 产生网关的IP地址
ipv4_net = ipv4_add[:-2]
ipv4_ran = str(random.choice(['1', '100', '254']))
ipv4_gw = ipv4_net + ipv4_ran

# 打印网关的IP地址
print('\n我们假设网关IP地址为最后一位为', ipv4_ran, '因此网关地址为:' + ipv4_gw + '\n')

# Ping网关
ping_result = 'PING 172.20.10.1 (172.20.10.1) 56(84) bytes of data.\n' \
              '64 bytes from 172.20.10.1: icmp_seq=1 ttl=64 time=5.34 ms\n' \
              '\n' \
              '--- 172.20.10.1 ping statistics ---\n' \
              '1 packets transmitted, 1 received, 0% packet loss, time 0ms\n' \
              'rtt min/avg/max/mdev = 5.343/5.343/5.343/0.000 ms\n'

re_ping_result = re.findall(r'\s+[1-9]\s+received', ping_result)
print(re_ping_result)
if re_ping_result:
    print('网关可达! ')
else:
    print('网关不可达! ')




