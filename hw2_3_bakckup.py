'''Homework 2_3 vanessa wong 01/29/2025'''
import sqlite3
import sys
import os
import csv


db_filename = 'session_2.db'
table_name  = 'weather_newyork'
csv_filename = 'weather_newyork.csv'

csv_file = open(csv_filename)
dreader = csv.DictReader(csv_file)
columns  = dreader.fieldnames

conn = sqlite3.connect(db_filename)
c = conn.cursor()

drop   = 'DROP TABLE IF EXISTS ' + table_name
create = 'CREATE TABLE ' + table_name +' (mean_tmp INT, precip FLOAT, events TEXT)'

c.execute(drop)
c.execute(create)

for row in dreader:
    c.execute('INSERT INTO  ' + table_name + '(mean_tmp, precip, events) VALUES (?,?,?)',
              (row['mean_temp'],row['precip'],row['events']))

csv_file.close()
conn.commit()
conn.close()