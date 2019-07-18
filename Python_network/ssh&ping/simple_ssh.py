# -*- coding: utf-8 -*-
"""
Created on 2019/6/21 17:22

File name   simple_ssh.py

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
    from argparse import ArgumentParser

    usage = 'Example: simple_ssh -i ipaddr -u username -p password -c command'

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-i", "--ipaddr", dest="ip", help="Target SSH Server", default='192.168.0.102', type=str)
    parser.add_argument("-u", "--username", dest="username", help="SSH Server username", default='root', type=str)
    parser.add_argument("-p", "--password", dest="password", help='SSH Server password', default='root', type=str)
    parser.add_argument("-o", "--port", dest="port", help="SSH Server Port", default="22", type=int)
    parser.add_argument("-c", "--command", dest="cmd", help='Shell Command',default='uname -a', type=str)
    parser.add_argument(nargs='?', dest="host", help="Specify an host", default="127.0.0.1", type=str)
    args = parser.parse_args()

    print(qytang_ssh(args.ip, args.username, args.password, args.port, args.cmd))
