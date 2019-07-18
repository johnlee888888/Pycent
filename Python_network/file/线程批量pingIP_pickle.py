# -*- coding: utf-8 -*-
"""
Created on 2019/6/26 17:01

File name   线程批量pingIP.py

@author: john lee
"""

import pickle
import datetime
from 线程批量pingIP import ping_scan


ip_addr = (ping_scan('192.168.107.0/30'))
time = datetime.datetime.now()
date_format = time.strftime("%Y-%m-%d")
clock_format = time.strftime("%H-%M-%S")
pkfile = open("scan_save_pickle_{0}_{1}.pl".format(date_format, clock_format), "wb")
pickle.dump(ip_addr, pkfile)
pkfile.close()

db_file = open("scan_save_pickle_2019-07-01_22-05-23.pl", "rb")
db = pickle.load(db_file)
print('网段中可达地址为:', db)



