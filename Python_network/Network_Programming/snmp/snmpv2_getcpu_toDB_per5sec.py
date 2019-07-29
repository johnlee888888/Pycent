# -*- coding: utf-8 -*-
"""
Created on 2019/7/25 13:30

File name   snmpv2_get.py

@author: john lee
"""
from pysnmp.hlapi import *
import psycopg2
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


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


devices = ['10.1.1.102']
community = 'lizyro'


def data_to_db():
    con_db = psycopg2.connect(database='pycent', user='admin', password='Pa$$w0rd', host='localhost')
    cursor = con_db.cursor()
    cursor.execute("select count(*) from pg_class where relname = 'cpu_total'")  # 查询整个数据库是否存在cpu_total
    check = cursor.fetchall()[0][0]  # 得到查询返回结果
    if check == 0:  # 如果没有查到此表
        cursor.execute("create table cpu_total (id integer primary key , time varchar(64), cpu int)")  # 创建cpu_total
        cursor.execute("CREATE SEQUENCE cpu_total_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1; "
                       "alter table cpu_total alter column id set default nextval('cpu_total_id_seq');")  # 写入数据时id位自增
    else:
        pass
    for device in devices:
        cpu5s = snmpv2_get(device, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.3.7', port=161)[1]

        cursor.execute("insert into cpu_total (time, cpu) values (%s,%s)", (datetime.now(), cpu5s))

    con_db.commit()


scheduler = BlockingScheduler()

scheduler.add_job(func=data_to_db, args=(),
                  trigger='cron', second='*/5', id='每五秒获取数据并写入到数据库!')

try:
    scheduler.start()
except KeyboardInterrupt:
    print('收到停止调度命令!正在退出!')


if __name__ == '__main__':
    pass
    # print('CPU_5秒利用率:', snmpv2_get('10.1.1.102', 'lizyro', '1.3.6.1.4.1.9.9.109.1.1.1.1.3.7', port=161)[1])
    # data_to_db()
