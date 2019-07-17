# -*- coding: utf-8 -*-
"""
Created on 2019/7/1 10:01

File name   找相同.py

@author: john lee
"""
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

print('方案一')

for x in list1:
    if x in list2:
        print(x, 'in List1 and List2')
    elif x not in list2:
        print(x, 'only in List1')


print('方案二')


def find_x(word):
    if word not in list2:
        print(word, 'only in List1')
    elif word not in list1:
        print(word, 'only in List2')
    else:
        print(word, 'in List1 and List2')


if __name__ == '__main__':
    find_x('aaa')
    find_x(111)
    find_x((4, 5))
    find_x(2.01)
