# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 17:08

File name   ssh.py

@author: john lee
"""
import paramiko


def qytang_ssh(ip, username, password, port=22, cmd='uname -a\nls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('192.168.0.100', 'john', 'cisc0123!'))
    print(qytang_ssh('192.168.0.100', 'john', 'cisc0123!', cmd='pwd'))
