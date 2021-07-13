import sqlite3

con = sqlite3.connect("login.db")
con.text_factory = bytes
cur = con.cursor()

# Return all results of query
cur.execute('SELECT * FROM logins')
res = cur.fetchall()

con.close()
