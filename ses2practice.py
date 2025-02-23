import sqlite3
import csv
import sys
import os
import argparse


# function to copy data from sql database to csv file
def sql_to_csv(db_name, table_name, csv_filename):

    db_filename = db_name
    tablename = table_name
    csvfilename = csv_filename

    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    csv_file = open(csvfilename, 'w', newline = '')

    q = 'SELECT * FROM ' + table_name
    #prepares a view of the query results for reading
    c.execute(q)

    data = c.fetchall()
    writer = csv.writer(csv_file)
    writer.writerows(data)

    return data
# end fundion
ret_value = sql_to_csv('session_2.db', 'revenue', 'revenu_from_db.csv')
print(ret_value)
