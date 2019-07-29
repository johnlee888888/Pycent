# -*- coding: utf-8 -*-
"""
Created on 2019/7/19 13:18

File name   flow_monitor.py

@author: john lee
"""
import re
import paramiko
import time
from matplotlib import pyplot as plt
import sys


def get_monitor_data(ip, port, username, password, cmd, wait_time, enable=''):
    protocols = []
    numbers = []
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(wait_time)
    result = chan.recv(2048).decode()
    time.sleep(wait_time)
    if re.match(r'\s+\w+.*(>)', result):
        chan.send('en'.encode())
        chan.send(b'\n')
        chan.send(enable.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        print('已成功进入路由器特权模式(有enable密码)!')
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        result_cmd = chan.recv(4096).decode()
        result_ssh = re.findall(r'\s+port\s+(ssh)\s+(\d+)', result_cmd)
        result_telnet = re.findall(r'\s+port\s+(telnet)\s+(\d+)', result_cmd)
        protocols.append(result_telnet[0][0])
        numbers.append(result_telnet[0][1])
        protocols.append(result_ssh[0][0])
        numbers.append(result_ssh[0][1])
    elif not re.match(r'\s+\w+.*(>)', result):
        print('需要输入enable密码')
        sys.exit()
    else:
        print('已成功进入路由器特权模式(无enable密码)!')
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        result_cmd = chan.recv(4096).decode()
        result_ssh = re.findall(r'\s+port\s+(ssh)\s+(\d+)', result_cmd)
        result_telnet = re.findall(r'\s+port\s+(telnet)\s+(\d+)', result_cmd)
        protocols.append(result_telnet[0][0])
        numbers.append(result_telnet[0][1])
        protocols.append(result_ssh[0][0])
        numbers.append(result_ssh[0][1])

    chan.close()
    ssh.close()

    plt.figure(figsize=(6, 6))
    # 将某部分爆炸出来, 使用括号, 将第一块分隔出来, 数值的大小是分割出来的与其他两块的间隙
    expload = (0.01, 0.08)

    patches, label_text, percent_text = plt.pie(numbers,
                                                expload,
                                                labels=protocols,
                                                labeldistance=1.1,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)

    # labeldistance, 文本的位置离原点有多远,1.1指1.1倍半径的位置
    # autopct, 圆里面的文本格式, %3.1f%%表示小数位有三位,整数有一位的浮点数
    # shadow, 饼是否有阴影
    # startangle, 起始角度, 0表示从0开始逆时针转,为第一块. 一般选择从90度开始比较好看
    # pctdistance, 百分比的txt离圆心的距离
    # patches, label_text, percent_text, 为了得到圆饼的返回值, percent_text饼图内部文本的, label_text饼图外lable的文本

    # 改变文本的大小
    # 方法是把每一个text遍历, 调用set size 方法设置他的属性
    for l in label_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20
    # 设置x, y 轴刻度一致, 这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    get_monitor_data('10.1.1.131', port=22, username='admin', password='admin',
                     enable='admin', wait_time=4,
                     cmd='show flow monitor li-monitor cache format table | beg APP')
