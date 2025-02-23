cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [ tup[0] for tup in cursor.fetchall() ]
print(f'tables:  {tables}')