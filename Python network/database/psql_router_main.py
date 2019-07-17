# -*- coding: utf-8 -*-
"""
Created on 2019/7/11 18:12

File name   psql_router_main.py

@author: john lee
"""
import psycopg2
import re
import hashlib
from ssh_connect import ssh_client

# 设备清单
device_list = ['192.168.107.130', '192.168.107.133']
# 用户名和密码
Username = 'admin'
Password = 'admin'


def get_config_md5(ip, username, password):
    run_config_raw = ssh_client(ip, username, password, cmd='show run')
    config = re.split(r'\r\n\s*hostname\s+\w+', run_config_raw)
    run_config = (run_config_raw.replace(config[0], '').strip())

    # 计算获取配置的md5值
    m = hashlib.md5()
    m.update(run_config.encode())
    md5_value = m.hexdigest()

    return run_config, md5_value


def write_config_md5_to_db():
    con_db = psycopg2.connect(database="pycent", user="admin", password="Pa$$w0rd", host="localhost")
    cursor = con_db.cursor()
    # 逐个迭代设备,写入到数据库
    for device in device_list:
        config_and_md5 = get_config_md5(device, Username, Password)
        cursor.execute("select * from config_md5 where ip=%(address)s", {'address': device})
        md5_result = cursor.fetchall()
        if not md5_result:
            # 如果设备的数据库条目不存在,就写入
            cursor.execute("insert into config_md5(ip, config, md5_config) values (%s,%s,%s) ",
                           (device, config_and_md5[0], config_and_md5[1]))
        else:
            # 如果之前备份的MD5与当前获取的MD5不匹配,就更新该条目
            if md5_result[0][2] != config_and_md5[1]:
                cursor.execute("update config_md5 set md5_config=%(md5)s where ip=%(address)s",
                               {'md5': config_and_md5[1], 'address': device})
                cursor.execute("update config_md5 set config=%(conf)s where ip=%(address)s",
                               {'conf': config_and_md5[0], 'address': device})
            else:   # 如果之前备份的MD5值与当前获取的MD5值匹配! 就略过
                continue

    cursor.execute("select * from config_md5")
    all_result = cursor.fetchall()
    # 打印查看IP和MD5值
    for x in all_result:
        print(x[0], x[2])

    con_db.commit()


if __name__ == '__main__':
    # print(get_config_md5('192.168.107.130', Username, Password))
    write_config_md5_to_db()
