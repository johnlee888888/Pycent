# -*- coding: utf-8 -*-
"""
Created on 2019/7/16 11:00

File name   gratuitous_ARP.py

@author: john lee
"""
from kamene.all import *

arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwtype=0x1,
                                                  op=2,
                                                  psrc='192.168.107.133',
                                                  hwsrc='14:1d:23:12:23:21',
                                                  pdst='192.168.107.133',
                                                  hwdst='ff:ff:ff:ff:ff:ff')
arp_packet.show()
print(arp_packet.getlayer(ARP).fields.get('pdst'))
result = sendp(arp_packet, iface='ens37', loop=True, inter=30)


# def arp_sender(src_ip, src_mac, dst_ip):
#     arp_packet = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwdst='0x1',
#                                                       op=2,
#                                                       psrc=src_ip,
#                                                       hwsrc=src_mac,
#                                                       pdst=dst_ip)
#     for x in range(5):
#         sendp(arp_packet, iface='ens37')
#         time.sleep(10)
#
#
# if __name__ == '__main__':
#     print(arp_sender('192.168.107.133', '14:1d:23:12:23:21', '192.168.107.133'))
