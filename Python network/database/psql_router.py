# -*- coding: utf-8 -*-
"""
Created on 2019/7/11 18:05

File name   psql_router.py

@author: john lee
"""
import psycopg2

con_db = psycopg2.connect(database="pycent", user="admin", password="Pa$$w0rd", host="localhost")
cursor = con_db.cursor()

cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5_config varchar (999))")

con_db.commit()
