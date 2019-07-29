# -*- coding: utf-8 -*-
"""
Created on 2019/7/25 16:15

File name   read_db_and_return_timelimit.py

@author: john lee
"""
import psycopg2
from matplotlib import pyplot as plt
import datetime


def read_db(db, name, passwd, ho, set_time=1):
    con_db = psycopg2.connect(database=db, user=name, password=passwd, host=ho)
    cursor = con_db.cursor()
    time_range = datetime.datetime.now() - datetime.timedelta(minutes=set_time)
    # print(time_range)
    cursor.execute("select time,mem_percent from mem_info where time > '{0}'".format(time_range))
    result_list = cursor.fetchall()
    return result_list


plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['font.family'] = 'sans-serif'


def plot_data(r1_mem):
    # 调节图形大小, 宽, 高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))  # 设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M:%S'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.02f%%'))
    ax.set_ylim(0, 100)  # Y轴取值设置0-100
    # 把Mem的数据,拆分为x轴的时间,与y轴的利用率
    x = []
    y = []

    for time, mem in r1_mem:
        x.append(time)
        y.append(mem)

    # 添加主题和注释
    plt.title('路由器MEM利用率')
    plt.xlabel('采集时间')
    plt.ylabel('MEM 利用率')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果有两套数据,可以在一幅图中绘制双线
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 保存到图片
    plt.savefig('result_mem.png')
    # 绘制图形
    plt.show()


if __name__ == '__main__':
    r1_mem = read_db(db='pycent', name='admin', passwd='Pa$$w0rd', ho='localhost')  # 得到数据库中的值
    # print(read_db(db='pycent', name='admin', passwd='Pa$$w0rd', ho='localhost'))
    plot_data(r1_mem)
