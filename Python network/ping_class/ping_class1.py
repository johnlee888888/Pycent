# -*- coding: utf-8 -*-
"""
Created on 2019/7/8 9:26

File name   ping_class.py

@author: john lee
"""
from ping_module import lee_ping
from kamene.all import *


class L1ping:
    def __init__(self, d_ip):
        self.d_ip = d_ip

    def src(self, s_ip):
        self.s_ip = s_ip

    def size(self, length):
        self.length = length

    def one(self):
        print(self.d_ip, lee_ping(self.d_ip))

    def ping(self):
        payload = str(self.length)
        ping_packet_1 = IP(dst=self.d_ip) / ICMP() / payload
        ping_result_1 = sr1(ping_packet_1, timeout=2, verbose=False)
        if ping_result_1:
            print('!' * 5)
        else:
            print('.' * 5)

    def ping_1(self, s_ip):
        self.s_ip = s_ip
        payload = str(self.length)
        ping_packet_1 = IP(src=self.s_ip, dst=self.d_ip) / ICMP() / payload
        ping_result_1 = sr1(ping_packet_1, timeout=2, verbose=False)
        if ping_result_1:
            print('!' * 5)
        else:
            print('.' * 5)


    def __str__(self):
        return '<{0} => dst_ip: {1}, size: {2}'.\
            format(self.__class__.__name__, self.d_ip, self.length)

if __name__ == '__main__':
    ping = L1ping('192.168.0.1')
    ping2 = Sip('192.168.0.1')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70-len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping)  # 打印类
    print_new('ping one for sure reachable')
    ping.one()   # ping一个包判断可达性
    print_new('ping five')
    ping.ping()  # 模拟正常ping程序ping五个包,'!'表示通,'.'表示不通
    print_new('set payload length')
    ping.length = 200   # 设置负载长度
    print(ping)  # 打印类
    ping.ping()  # 使用修改长度的包进行ping测试
    print_new('set ping src ip address')
    ping.s_ip = '192.168.0.109'   # 修改源IP地址
    print(ping2)   # 打印类
    ping.ping()   # # 使用修改长度又修改源的包进行ping测试
    


