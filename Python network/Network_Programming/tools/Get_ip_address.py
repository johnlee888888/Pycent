# -*- coding: utf-8 -*-
"""
Created on 2019/7/14 14:18

File name   Get_ip_address.py

@author: john lee
"""
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
import platform
import pprint


def get_ip_addr(ifname):
    if platform.system() == 'Linux':
        return ifaddresses(ifname)[2][0]['addr']
    elif platform.system() == 'Windows':
        from win_ifname import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        return ifaddresses(if_id)[2][0]['addr']
    else:
        print('操作系统不支持,本脚本只能在Linux或者Windows环境下运行')


def get_ipv6_addr(ifname):
    if platform.system() == 'Linux':
        return ifaddresses(ifname)[10][0]['addr']
    elif platform.system() == 'Windows':
        from win_ifname import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        return ifaddresses(if_id)[23][0]['addr']
    else:
        print('操作系统不支持,本脚本只能在Linux或者Windows环境下运行')


if __name__ == '__main__':
    pprint.pprint(get_ip_addr('ens33'), indent=4)
    pprint.pprint(get_ipv6_addr('ens33'), indent=4)
    # pprint.pprint(get_ip_addr('WLAN'), indent=4)
    # pprint.pprint(get_ipv6_addr('WLAN'), indent=4)
