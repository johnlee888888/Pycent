# -*- coding: utf-8 -*-
"""
Created on 2019/7/15 16:25

File name   ipv6_tools.py

@author: john lee
"""
import re
# import ipaddress


def full_ipv6(ipv6):
    ipv6_section = ipv6.split(':')
    ipv6_section_len = len(ipv6.split(':'))

    if ipv6_section.index(''):
        null_location = ipv6_section.index('')
        ipv6_section.pop(null_location)
        add_section = 8 - ipv6_section_len + 1

        for x in range(add_section):
            ipv6_section.insert(null_location, '0000')

        new_ipv6 = []
        for s in ipv6_section:
            if len(s) < 4:
                new_ipv6.append((4 - len(s)) * '0' + s)
            else:
                new_ipv6.append(s)
        return ':'.join(new_ipv6)
    else:
        return ipv6


def solicited_node_multicast_address(ipv6):
    return 'FF02::1:FF' + full_ipv6(ipv6)[-7:]


def mac_to_ipv6_linklocal(mac):
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    high1 = mac_value >> 24 & 0xff
    low1 = mac_value >> 16 & 0xff
    low2 = mac_value & 0xffff
    return 'fe80::{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2, high1, low1, low2)


def ipv6_to_mac(ipv6):
    ipv6_address = full_ipv6(ipv6)
    last_4_sections = ipv6_address.split(":")[-4:]
    mac_1 = int(last_4_sections[0][:2], 16) ^ 0x02
    mac_2 = int(last_4_sections[0][2:], 16)
    mac_3 = int(last_4_sections[1][:2], 16)
    mac_4 = int(last_4_sections[2][2:], 16)
    mac_5 = int(last_4_sections[3][:2], 16)
    mac_6 = int(last_4_sections[3][2:], 16)

    return '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(mac_1, mac_2, mac_3, mac_4, mac_5, mac_6)


def mac_to_eui64(mac, prefix):
    # print()
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    # print(mac_value)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    high1 = mac_value >> 24 & 0xff
    low1 = mac_value >> 16 & 0xff
    low2 = mac_value & 0xffff

    host_id = '{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2, high1, low1, low2)

    net = prefix.split('/')[0]

    return net + host_id


if __name__ == '__main__':
    print(mac_to_eui64(mac='06:b2:4a:00:00:9f', prefix='2001:db8:100::/64'))
    print(mac_to_ipv6_linklocal('1d:2e:c1:99:01:42'))
    print(solicited_node_multicast_address('2001::f107:94ac:2717:a736'))
