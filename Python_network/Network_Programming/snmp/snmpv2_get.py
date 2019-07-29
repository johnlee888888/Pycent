# -*- coding: utf-8 -*-
"""
Created on 2019/7/25 13:30

File name   snmpv2_get.py

@author: john lee
"""
from pysnmp.hlapi import *


def snmpv2_get(ip, community, oid, port=161):
    # varBinds是列表, 列表中的每个元素的类型是ObjectType (该类型的对象表示MIB Variable)
    errorIndication, errorStatus, errorindex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))
               )
    )
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('{0} at {1}'.format(errorStatus, errorindex and varBinds[int(errorindex)-1][0] or '?'))
    # 如果返回结果有多行,需要拼接后返回
    result = ''

    for varBind in varBinds:
        result = result + varBind.prettyPrint()  # 返回结果!
    # 返回的为一个元组,OID与字符串结果
    return result.split('=')[0].strip(), result.split('=')[1].strip()


if __name__ == '__main__':
    # 系统描述
    # print('CPU_5秒利用率:', snmpv2_get('10.1.1.102', 'lizyro', '1.3.6.1.4.1.9.9.109.1.1.1.1.3.7', port=161)[1])
    print('MEM_可用:', snmpv2_get('10.1.1.102', 'lizyro', '1.3.6.1.4.1.9.9.48.1.1.1.6.1', port=161)[1])
    print('MEM_已用:', snmpv2_get('10.1.1.102', 'lizyro', '1.3.6.1.4.1.9.9.48.1.1.1.5.1', port=161)[1])
