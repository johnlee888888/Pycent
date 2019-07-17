# -*- coding: utf-8 -*-
"""
Created on 2019/7/8 9:26

File name   ping_class.py

@author: john lee
"""
from kamene.all import *


class L1ping:
    def __init__(self, d_ip):
        self.d_ip = d_ip
        self.length = 100
        self.s_ip = ''

    def __str__(self):
        if not self.s_ip:
            return '<{0} => dst_ip: {1}, size: {2}'.\
                format(self.__class__.__name__, self.d_ip, self.length)
        else:
            return '<{0} => src_ip: {1} dst_ip: {2}, size: {3}'.\
                format(self.__class__.__name__, self.s_ip, self.d_ip, self.length)

    def pkt(self):
        payload = (b'1' * self.length)
        if self.s_ip:
            self.packet = IP(src=self.s_ip, dst=self.d_ip) / ICMP() / payload
        else:
            self.packet = IP(dst=self.d_ip) / ICMP() / payload

    def one(self):
        self.pkt()
        ping_result_one = sr1(self.packet, timeout=2, verbose=False)
        if ping_result_one:
            print(self.d_ip, '可达!')
        else:
            print(self.d_ip, '不可达!')

    def ping(self, repeat=5, y='!', n='.'):
        self.pkt()
        for x in range(repeat):
            ping_result_five = sr1(self.packet, timeout=2, verbose=False)
            if ping_result_five:
                print(y, flush=True, end='')
            else:
                print(n, flush=True, end='')
        print('\t')


class NewPing(L1ping):
    def ping(self, repeat=5, y='+', n='?'):
        self.pkt()
        for x in range(repeat):
            ping_result_five = sr1(self.packet, timeout=2, verbose=False)
            if ping_result_five:
                print(y, flush=True, end='')
            else:
                print(n, flush=True, end='')
        print('\t')


if __name__ == '__main__':
    ping = L1ping('192.168.0.1')
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
    print(ping)   # 打印类
    ping.ping()   # 使用修改长度又修改源的包进行ping测试
    print_new('new class NewPing', '=')
    NewPing = NewPing('192.168.1.253')   # 使用新的类NewPing(通过继承L1ping类产生)产生实例!
    NewPing.length = 300
    print(NewPing)   # 打印类
    NewPing.ping()   # NewPing类自定义过ping()这个方法, '+'表示通,'?'表示不通
