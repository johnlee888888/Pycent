# -*- coding: utf-8 -*-
"""
Created on 2019/6/5 15:42

File name   ssh设备.py

@author: john lee
"""
import paramiko


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.100', port=22, username='john', password='cisc0123!',
            timeout=5, compress=True)
stdin, stdout, stderr = ssh.exec_command('uname -a\nls')
x = stdout.read().decode()
print(x)
