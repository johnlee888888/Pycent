# -*- coding: utf-8 -*-
"""
Created on 2019/6/9 21:42

File name   创建类.py

@author: john lee
"""


class LEE:
    def __init__(self, name, age, pay, worktime, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.worktime = worktime
        self.job = job

    # 建立处理数据的方法
    def getlastname(self):
        return self.name.split()[-1]

    # 加工资的方法
    def giveraise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    jack = LEE('jack lee', 30, 40000, 2, job='network')
    susan = LEE('susan', 20, 20000, 1, job='sales')
    jack.pay += 10000
    print(jack.job, jack.pay)
    print(susan.worktime, susan.job)
    print(jack.name.split()[-1])
    print(jack.getlastname())
    jack.giveraise(0.2)
    print(jack.pay)
