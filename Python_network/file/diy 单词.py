# -*- coding: utf-8 -*-
"""
Created on 2019/6/22 17:27

File name   diy 单词.py

@author: john lee
"""
word = 'tracer'

word2 = ((word + '-').strip('t') + (word.replace('racer', '') + 'y'))


print(word2)
