# -*- coding: utf-8 -*-
"""
Created on 2019/7/23 13:55

File name   histogram.py

@author: john lee
"""

from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['font.family'] = 'sans-serif'
colorlist = ['r', 'g', 'b', 'y']


def mat_histogram(size_list, name_list):
    # 调节图形大小, 宽, 高
    plt.figure(figsize=(6, 6))

    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=colorlist)

    # 竖向柱状图
    plt.bar(name_list, size_list, width=0.5, color=colorlist)

    # 添加主题和注释
    plt.title('协议与带宽分布')  # 主题
    plt.xlabel('带宽 (M/s)')  # X轴注释
    plt.ylabel('协议')  # Y轴注释

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


if __name__ == '__main__':
    counters = [54, 39, 41, 22]
    protocols = ['ssh协议', 'telnet协议', 'rdp协议', 'Rlogin协议']
    mat_histogram(counters, protocols)
