# -*- coding: utf-8 -*-
"""
Created on 2019/7/4 15:43

File name   登录并计算MD5.py

@author: john lee
"""
from ssh_connect import qytang_ssh
import re
import hashlib
import time


def get_dev_config(ip, username='admin', password='admin'):
    try:
        get_conf = qytang_ssh(ip, username, password, cmd='show run')
        config = re.split(r'\r\nhostname \S+\r\n', get_conf)
        running = get_conf.replace(config[0], '').strip()
        return running

    except Exception:
        return


def check_dev_diff(ip, username='admin', password='admin'):
    before_md5 = ''
    while True:
        try:
            m = hashlib.md5()
            m.update(str(get_dev_config(ip, username, password)).encode())
            md5 = m.hexdigest()
            time.sleep(5)
            print(md5)
            if not before_md5:
                before_md5 = md5
            elif before_md5 != md5:
                print('MD5 value changed')
                break
            time.sleep(5)
        except KeyboardInterrupt:
            print('收到停止命令,请稍后!')
            time.sleep(1)
            print('退出程序!')
            break


if __name__ == '__main__':
    # print(get_dev_config('192.168.107.130', username='admin', password='admin'))
    check_dev_diff('192.168.107.130', username='admin', password='admin')
