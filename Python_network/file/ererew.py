# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 20:23

File name   ererew.py

@author: john lee
"""
from scapy.all import *
import logging
import paramiko


def qytang_ping(ip):
    ping_packet = IP(dst=ip) / ICMP()
    ping_result = scapy.all.sr1(ping_packet, timeout=2, verbose=False)
    if ping_result:
        return '可达!'
    else:
        print(ip, '不通')
        return '不通'


def qytang_ssh(ip, username, password, port=22, cmd='uname -a\nls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    ip = '192.168.0.100'
    if "可达" in qytang_ping(ip):
        print(ip, '可达')
        print('登录', ip, '执行命令 ls 的回显结果如下:')
        print(qytang_ssh(ip, 'john', 'cisc0123!', cmd='ls'))
    else:
        print(ip, '不可达')
