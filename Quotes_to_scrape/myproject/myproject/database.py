import sqlite3

con = sqlite3.connect("myquotes.db")
c = con.cursor()
c.execute(""" create table tbl_quotes (title text, author text, tags text)""")
con.commit()
con.close()