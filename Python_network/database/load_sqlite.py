# -*- coding: utf-8 -*-
"""
Created on 2019/7/10 23:10

File name   load_sqlite.py

@author: john lee
"""
import sqlite3


con_db = sqlite3.connect('students5.sqlite')
cursor = con_db.cursor()

user_notify = """
请输入查询选项:
输入1 :   查询整个数据库
输入2 :   基于姓名查询
输入3 :   基于年龄查询
输入4 :   基于作业数查询
输入0 :   退出
"""
while True:
    try:
        print(user_notify)
        user_input = input('请选择:')
        if user_input == '0':
            break
        elif user_input == '1':
            cursor.execute("select * from qytang_homework_info")
            yourresults = cursor.fetchall()
            for students in yourresults:
                print('{0:<5}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}'
                      .format('学员姓名:', students[0], '学员年龄:', students[1], '学员作业数:', students[2]))
        elif user_input == '2':
            user_sn = input('请输入学员姓名:')
            if not user_sn:
                continue
            cursor.execute("select * from qytang_homework_info where 姓名 = ?", (user_sn,))
            yourresults = cursor.fetchall()
            if not yourresults:
                print('学员信息未找到!')
            for students in yourresults:
                print('{0:<5}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}'
                      .format('学员姓名:', students[0], '学员年龄:', students[1], '学员作业数:', students[2]))
        elif user_input == '3':
            user_age = input('搜索大于输入年龄的学员,请输入学员年龄:')
            if not user_age:
                continue
            cursor.execute("select * from qytang_homework_info where 年龄 > ?", (user_age,))
            yourresults = cursor.fetchall()
            if not yourresults:
                print('学员信息未找到!')
            for students in yourresults:
                print('{0:<5}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}'
                      .format('学员姓名:', students[0], '学员年龄:', students[1], '学员作业数:', students[2]))
        elif user_input == '4':
            user_homework = input('搜索大于输入作业数的员,请输入作业数量:')
            if not user_homework:
                continue
            cursor.execute("select * from qytang_homework_info where 作业数 > ?", (user_homework,))
            yourresults = cursor.fetchall()
            if not yourresults:
                print('学员信息未找到!')
            for students in yourresults:
                print('{0:<5}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}'
                      .format('学员姓名:', students[0], '学员年龄:', students[1], '学员作业数:', students[2]))
        else:
            print('输入错误!请重新输入!')

    except KeyboardInterrupt:
        print('收到停止命令,退出程序!')
        break
