# -*- coding: utf-8 -*-
"""
Created on 2019/6/26 17:01

File name   线程批量pingIP.py

@author: john lee
"""
import ipaddress
import pickle
import datetime
from multiprocessing.pool import ThreadPool
from ping_modules_new import qytang_ping


def ping_scan(network):
    pool = ThreadPool(processes=150)
    net = ipaddress.ip_network(network)

    result_obj_dict = {}

    for ip in net:
        result_obj = pool.apply_async(qytang_ping, args=(str(ip),))
        result_obj_dict[str(ip)] = result_obj

    pool.close()
    pool.join()

    active_ip = []

    for ip, obj in result_obj_dict.items():
        if ip and obj.get() == '通!':
            active_ip.append(ip)

    return active_ip


if __name__ == '__main__':
    ip_addr = (ping_scan('192.168.107.0/30'))
    time = datetime.datetime.now()
    date_format = time.strftime("%Y-%m-%d")
    clock_format = time.strftime("%H-%M-%S")
    pkfile = open("scan_save_pickle_{0}_{1}.pl".format(date_format, clock_format), "wb")
    pickle.dump(ip_addr, pkfile)
    pkfile.close()



