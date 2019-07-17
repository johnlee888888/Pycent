# -*- coding: utf-8 -*-
"""
Created on 2019/7/14 14:46

File name   win_ifname.py

@author: john lee
"""
import netifaces as ni
import winreg as reg


def get_connection_name_from_guid(iface_guids):
    # 产生接口的名字清单, 默认全部填写'(unknown)'
    iface_dict = {}
    # 打开"HKEY_LOCAL_MACHINE"
    registry = reg.ConnectRegistry(None, reg.HKEY_LOCAL_MACHINE)
    registry_key = reg.OpenKey(registry, r'SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}')
    for key in range(len(iface_guids)):
        try:
            # 尝试读取每一个接口ID下对应的Name
            # print(iface_guids[key])
            reg_subkey = reg.OpenKey(registry_key, iface_guids[key] + r'\Connection')
            # 如果存在Name,写入iface_dict
            iface_dict[reg.QueryValueEx(reg_subkey, 'Name')[0]] = iface_guids[key]
        except FileNotFoundError:
            pass
    # 返回iface_dict
    # print(iface_dict)
    return iface_dict


def win_from_name_get_id(interface):
    x = ni.interfaces()
    # print(x)
    return get_connection_name_from_guid(x).get(interface)


if __name__ == '__main__':
    # get_connection_name_from_guid('{4D36E972-E325-11CE-BFC1-08002BE10318}')
    print(win_from_name_get_id('WLAN'))
