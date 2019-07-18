# -*- coding: utf-8 -*-
"""
Created on 2019/6/21 18:07

File name   test1.py

@author: john lee
"""


def qyt_arg(ip, username, password, cmd):
    print(ip)
    print(username)
    print(password)
    print(cmd)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'Example: simple_ssh -i ipaddr -u username -p password -c command'

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-i", "--ipaddr", dest='ip', help="Target SSH Server", default='1.1.1.1', type=str)
    parser.add_argument("-u", "--username", dest="username", help="SSH Server username", default='admin', type=str)
    parser.add_argument("-p", "--password", dest='password', help='SSH Server password', default='123', type=int)
    parser.add_argument("-c", "--command", dest='cmd', help='Shell Command',default='uname -a', type=str)
    parser.add_argument(nargs='?', dest="host", help="Specify an host", default="127.0.0.1", type=str)
    args = parser.parse_args()

    qyt_arg(args.ip, args.username, args.password, args.cmd)