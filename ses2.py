import sqlite3

db_filename = 'session_2.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()     # represents you agent when communication with database
results = list(c) # list constructs loops over
q = 'SELECT * FROM revenue'
#prepares a view of the query results for reading
c.execute(q)
row = c.fetchone()
print(row)
print(c.fetchmany(3))
print(c.fetchall())
company ="O'Hanlon"
state = "CA"
cost = 235.9
query = f"INSERT INTO revenue VALUES (?,?,?)"
c.execute(query, (company, state, cost))
conn.commit()

