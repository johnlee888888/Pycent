# -*- coding: utf-8 -*-
"""
Created on 2019/7/18 9:35

File name   protocols.py

@author: john lee
"""
from matplotlib import pyplot as plt
# import matplotlib
# print(matplotlib.matplotlib_fname())
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_bing(size_list, name_list):
    # 调节图形大小,宽,高
    plt.figure(figsize=(6, 6))
    # 将某部分爆炸出来, 使用括号, 将第一块分隔出来, 数值的大小是分割出来的与其他两块的间隙
    expload = (0.03, 0.02, 0.01, 0.01)

    patches, label_text, percent_text = plt.pie(size_list,
                                                expload,
                                                labels=name_list,
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
    counters = [54, 29, 11, 6]
    protocols = ['ssh协议', 'telnet协议', 'rdp协议', 'Rlogin协议']
    mat_bing(counters, protocols)
