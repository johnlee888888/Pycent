# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:50:10 2019

@author: ydboo
"""
import string
import random

s = string.hexdigits


def create_mac():
    mac = '14'
    for i in range(5):
        n = "".join(random.sample(s, 2)).lower()
        mac += '-'+n
    return mac


if __name__ == '__main__':
    print(create_mac())
