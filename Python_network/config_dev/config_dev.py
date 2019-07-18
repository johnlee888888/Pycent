# -*- coding: utf-8 -*-
"""
Created on 2019/7/6 17:19

File name   config_dev.py

@author: john lee
"""
import paramiko
import time
import re


def config_l3_dev(ip, username='admin', password='admin', port=22, enable='',
                  wait_time=2, cmd_list='show users', verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(wait_time)
    result = chan.recv(2048).decode()
    time.sleep(wait_time)
    if re.match(r'\s+\w+.*(>)', result):
        chan.send('en'.encode())
        chan.send(b'\n')
        chan.send(enable.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        print('已成功进入路由器特权模式(有enable密码)!')
        for x in cmd_list:
            chan.send(x.encode())
            chan.send(b'\n')
            time.sleep(wait_time)
            if verbose is True:
                print(chan.recv(4096).decode())
    elif not re.match(r'\s+\w+.*(>)', result):
        print('需要输入enable密码')
    else:
        print('已成功进入路由器特权模式(无enable密码)!')
        for x in cmd_list:
            chan.send(x.encode())
            chan.send(b'\n')
            time.sleep(wait_time)
            if verbose is True:
                print(chan.recv(4096).decode())
    chan.close()
    ssh.close()


if __name__ == '__main__':
    # config_l3_dev('192.168.107.130', username='admin', password='admin', enable='admin',
    #               cmd_list=['terminal len 0',
    #               'show vers',
    #               'config t',
    #               'router ospf 1',
    #               'network 2.2.2.2 0.0.0.0 area 0'],
    #               wait_time=6)
    config_l3_dev('192.168.107.131', username='admin', password='admin', enable='admin',
                  cmd_list=['terminal len 0',
                            'show vers',
                            'config t',
                            'router ospf 1',
                            'network 3.3.3.3 0.0.0.0 area 0'],
                  wait_time=6, verbose=True)
