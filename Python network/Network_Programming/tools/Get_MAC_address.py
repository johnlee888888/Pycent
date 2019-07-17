# -*- coding: utf-8 -*-
"""
Created on 2019/7/14 14:18

File name   Get_ip_address.py

@author: john lee
"""
import netifaces
import platform
import pprint
pp = pprint.PrettyPrinter(indent=4)


def get_mac_addr(ifname):
    if platform.system() == 'Linux':
        return netifaces.ifaddresses(ifname)[netifaces.AF_LINK][0]['addr']
    elif platform.system() == 'Windows':
        from win_ifname import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        # pp.pprint(netifaces.ifaddresses(if_id))
        # print(netifaces.AF_LINK)
        return netifaces.ifaddresses(if_id)[netifaces.AF_LINK][0]['addr']
    else:
        print('操作系统不支持,本脚本只能在Linux或者Windows环境下运行')


if __name__ == '__main__':
    pprint.pprint(get_mac_addr('ens33'), indent=4)
    # pprint.pprint(get_mac_addr('WLAN'), indent=4)
