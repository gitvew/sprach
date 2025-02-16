"""Homework 2_1  vanessa wong 02/03/2025"""
import sqlite3
import csv
import sys
import os
import argparse

# function to copy data from sql database to csv file
def sql_to_csv(db_name, table_name, csv_filename):

    db_filename = db_name
    tablename   = table_name
    csvfilename = csv_filename

    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    csv_file = open(csvfilename, 'w', newline = '')

    q = 'SELECT * FROM ' + table_name
    c.execute(q)

    writer = csv.writer(csv_file)

    columns = [desc[0] for desc in c.description]
    writer.writerow(columns)

    data = c.fetchall()
    writer.writerows(data)

    csv_file.close()
    conn.close()

    return data

sql_to_csv('session_2.db', 'revenue', 'revenue_from_db.csv')

