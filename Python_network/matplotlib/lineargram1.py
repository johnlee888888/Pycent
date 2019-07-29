# -*- coding: utf-8 -*-
"""
Created on 2019/7/23 14:26

File name   lineargram.py

@author: john lee
"""
import datetime
import random
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_lineargram(r1_usage_list, r2_usage_list):
    # 调节图形大小, 宽, 高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))  # 设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    # 把cpu usage_list的数据,拆分为x轴的时间,与y轴的利用率
    x = []
    y = []
    x2 = []
    y2 = []
    for time, cpu in r1_usage_list:
        x.append(time)
        y.append(cpu)
    for time2, cpu2 in r2_usage_list:
        x2.append(time2)
        y2.append(cpu2)
    # 添加主题和注释
    plt.title('路由器CPU利用率')
    plt.xlabel('采集时间')
    plt.ylabel('cpu 利用率')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果有两套数据,可以在一幅图中绘制双线
    ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 保存到图片
    plt.savefig('result2.png')
    # 绘制图形
    plt.show()


if __name__ == '__main__':
    r1list_cpu = [(datetime.datetime.now() - datetime.timedelta(hours=12), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=11), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=10), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=9), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=8), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=7), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=6), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=5), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=4), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=3), random.randint(0, 100)),
                  (datetime.datetime.now(), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=3), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=4), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=5), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=6), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=7), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=8), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=9), random.randint(0, 100))]

    r2list_cpu = [(datetime.datetime.now() - datetime.timedelta(hours=12), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=11), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=10), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=9), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=8), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=7), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=6), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=5), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=4), random.randint(0, 100)),
                  (datetime.datetime.now() - datetime.timedelta(hours=3), random.randint(0, 100)),
                  (datetime.datetime.now(), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=3), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=4), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=5), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=6), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=7), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=8), random.randint(0, 100)),
                  (datetime.datetime.now() + datetime.timedelta(hours=9), random.randint(0, 100))]
    print(r1list_cpu)
    # mat_lineargram(r1list_cpu, r2list_cpu)
