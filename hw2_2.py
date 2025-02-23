'''Homework 2_2 vanessa wong 01/29/2025'''
import sqlite3
import sys
import os


db_filename = 'session_2.db'
table_name  = 'weather_newyork'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

drop   = 'DROP TABLE IF EXISTS ' + table_name
create = 'CREATE TABLE ' + table_name +' (mean_tmp INT, precip FLOAT, events TEXT)'

c.execute(drop)
c.execute(create)

conn.commit()
conn.close()