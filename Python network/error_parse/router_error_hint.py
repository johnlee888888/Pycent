# -*- coding: utf-8 -*-
"""
Created on 2019/7/12 16:22

File name   router_error_hint.py

@author: john lee
"""
from ssh_connect import ssh_client


def login_dev(ip, username, password, port, cmd):
    try:
        config = ssh_client(ip, username, password, port, cmd)
        if 'Line has invalid autocommand' in config:
            return '命令不能被执行! 请检查命令或者用户权限!\nNone'
        elif 'Ambiguous command' in config:
            return '命令输入不完整!请检查后重新输入!'
        else:
            return config
    except Exception as e:
        if str(e).strip() == 'Authentication failed.':
            print('认证错误', e)
        elif str(e).strip() == 'timed out':
            print('连接超时', e)
        elif '[Errno None] Unable to connect to port ' in str(e).strip():
            print('SSH 请求被管理性过滤,或者IP不可达!', e)


if __name__ == '__main__':
    print(login_dev('192.168.107.131', username='admin', password='admin', port=22, cmd='show run'))
