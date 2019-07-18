# -*- coding: utf-8 -*-
"""
Created on 2019/7/3 20:36

File name   ping_ssh_router.py

@author: john lee
"""
from ping_module import qytang_ping
from ssh_connect import qytang_ssh
import re
import pprint


def net_dev_test(*ips, username='admin', password='admin'):
    device_if_dict = {}
    interface_dict = {}
    for ip_add in ips:
        if qytang_ping(ip_add) == '可达':
            values = qytang_ssh(ip_add, username, password, cmd='show ip int bri')
            ww = (values.split('\n'))
            info_int = re.match(r'.*(\w{8,15}\d+/\d+).*(\w{8,15}\d+/\d+).*'
                                r'(\w{8,15}\d+/\d+).*(\w{8,15}\d+)', str(ww)).groups()
            info_ip = re.match(r'.*\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*'
                               r'\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*'
                               r'\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*'
                               r'\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', str(ww)).groups()
            interface_dict = {info_int[0]: info_ip[0], info_int[1]: info_ip[1], info_int[2]: info_ip[2]
                              , info_int[3]: info_ip[3]}
            device_if_dict[str(ip_add)] = interface_dict

        else:
            values_2 = {}
            device_if_dict[str(ip_add)] = values_2
            break

    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(net_dev_test('192.168.107.130', '192.168.107.131', username='admin', password='admin'), indent=4)

