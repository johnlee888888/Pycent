# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:50:10 2019

@author: ydboo
"""
import random

# 产生一段随机IP
section1 = random.randint(200, 240)
section2 = random.randint(10, 100)
section3 = random.randint(100, 155)
section4 = random.randint(55, 199)

random_ip = (str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4))

print(random_ip)

