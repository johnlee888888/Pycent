# -*- coding: utf-8 -*-
"""
Created on 2019/7/25 16:15

File name   read_db_and_return_timelimit.py

@author: john lee
"""
import psycopg2
from matplotlib import pyplot as plt
import datetime


def read_db():
    con_db = psycopg2.connect(database="pycent", user="admin", password="Pa$$w0rd", host="localhost")
    cursor = con_db.cursor()
    cursor.execute("select time from cpu_total")
    time_result = cursor.fetchall()
    cursor.execute("select cpu from cpu_total")
    cpu_result = cursor.fetchall()
    result_list = list(time_result), list(cpu_result)
    return result_list


plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['font.family'] = 'sans-serif'


def plot_data(r1):
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
    ax.set_ylim(0, 100)  # Y轴取值设置0-100
    # 把cpu usage_list的数据,拆分为x轴的时间,与y轴的利用率
    x = []
    y = []

    for time, cpu in r1:
        x.append(time)
        y.append(cpu)

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
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 保存到图片
    plt.savefig('result2.png')
    # 绘制图形
    plt.show()


if __name__ == '__main__':
    list1 = read_db()[0]  # 得到时间
    list2 = read_db()[1]  # 得到利用率
    r1 = [(datetime.datetime.strptime(a[0], "%Y-%m-%d %H:%M:%S.%f"), b[0]) for a, b in zip(list1, list2)]  # 将时间和利用率加入列表
    plot_data(r1)  # 传入绘图函数
