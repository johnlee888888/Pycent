# -*- coding: utf-8 -*-
"""
Created on 2019/6/16 15:41

File name   sys_argv.py

@author: john lee
"""


def sys_argv(a, b):
    print(int(a) + int(b))


if __name__ == '__main__':
    import sys
    print(sys.argv[0])
    sys_argv(sys.argv[1], sys.argv[2])
