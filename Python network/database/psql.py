# -*- coding: utf-8 -*-
"""
Created on 2019/7/11 16:13

File name   psql.py

@author: john lee
"""
import psycopg2

con_db = psycopg2.connect(database="pycent", user="admin", password="Pa$$w0rd", host="localhost", port="5432")
cursor = con_db.cursor()


# cursor.execute("Create table student1(id int,name varchar,sex varchar);")
# cursor.execute("insert into student1(id, name, sex) values (1, 'john', 'male')")
homework_dict = [{'姓名': '刘德华', '年龄': 37, '作业数': 1},
                 {'姓名': '张学友', '年龄': 33, '作业数': 5},
                 {'姓名': '黎明', '年龄': 32, '作业数': 10},
                 {'姓名': '郭富城', '年龄': 30, '作业数': 15}]
cursor.execute("Create table students1(姓名 varchar(40),年龄 int,作业数 int);")
for students in homework_dict:
    name = students['姓名']
    age = students['年龄']
    work = students['作业数']
    cursor.execute("insert into students1(姓名, 年龄, 作业数) values(%s,%s,%s)", (name, age, work))

con_db.commit()
