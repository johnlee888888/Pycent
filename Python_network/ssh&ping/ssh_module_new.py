# -*- coding: utf-8 -*-
"""
Created on 2019/7/2 17:21

File name   ssh_module_new.py

@author: john lee
"""
import paramiko
import re


def ssh_client(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


def ssh_get_route(ip, username, password, port=22, cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    route = stdout.read().decode().split('/n')
    gw = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+(UG)'
                  , str(route)).groups()
    return gw[0]


if __name__ == '__main__':
    print(ssh_client('192.168.107.128', 'root', 'root'))
    print(ssh_client('192.168.107.128', 'root', 'root', cmd='pwd'))
    print('网关为:')
    print(ssh_get_route('192.168.107.128', 'root', 'root'))
