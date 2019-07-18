# -*- coding: utf-8 -*-
"""
Created on 2019/7/10 17:45

File name   sqlite.py

@author: john lee
"""
import sqlite3


homework_dict = [{'姓名': '刘德华', '年龄': 37, '作业数': 1},
                 {'姓名': '张学友', '年龄': 33, '作业数': 5},
                 {'姓名': '黎明', '年龄': 32, '作业数': 10},
                 {'姓名': '郭富城', '年龄': 30, '作业数': 15}]

# 连接 SQLite数据库
con_db = sqlite3.connect('students5.sqlite')
cursor = con_db.cursor()

# 执行创建表的任务
cursor.execute("create table qytang_homework_info (姓名 varchar(40), 年龄 int, 作业数 int)")

# 读取Python字典数据,并逐条写入SQLite数据库
for student in homework_dict:
    name = student['姓名']
    age = student['年龄']
    homework = student["作业数"]
    params = (name, age, homework)
    cursor.execute("insert into qytang_homework_info(姓名,年龄,作业数) values (?, ?, ?)", params)

con_db.commit()


