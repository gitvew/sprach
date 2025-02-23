'''Homework 2_4 vanessa wong 02/03/2025'''
import sqlite3
import sys
import os
import csv
import json


db_filename   = 'session_2.db'
table_name    = 'weather_newyork'
json_filename = 'weather_newyork_dod.json'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

drop   = 'DROP TABLE IF EXISTS ' + table_name
create = 'CREATE TABLE ' + table_name +' (dt DATE, mean_tmp INT, precip FLOAT, events TEXT)'

c.execute(drop)
c.execute(create)

json_file = open(json_filename)
json_data = json.load(json_file)

for item in json_data:
    for jkey in json_data.keys():
        jdate = jkey
    mean_temp = json_data[item]['mean_temp']
    precip    = json_data[item]['precip']
    events    = json_data[item]['events']

    if precip  == 'T':
        precip = None
    c.execute('INSERT INTO  ' + table_name + '(dt, mean_tmp, precip, events) VALUES (?,?,?,?)',
              (jdate, mean_temp, precip, events))


json_file.close()
conn.commit()
conn.close()