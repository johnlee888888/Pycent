# -*- coding: utf-8 -*-
"""
Created on 2019/6/24 15:25

File name   创建数据库.py

@author: john lee
"""
import sqlite3

# 赋值数据库连接的文件名
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
# 创建test页
cursor.execute('create table test(t1 int,t2 varchar(40))')
# 插入第一行第一列和第二列
cursor.execute("insert into test(t1,t2) values(11, 'welcome to qyt')")
# 插入第二行第一列和第二列
cursor.execute("insert into test(t1,t2) values (12, 'study python')")
# 查询
cursor.execute("select * from test")
# 赋值查询结果
yourresult = cursor.fetchall()
for i in yourresult:
    print(i)
conn.commit()