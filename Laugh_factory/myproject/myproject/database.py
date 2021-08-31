import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mydb'
)
c = con.cursor()
c.execute(""" create table tbl_myjokes (joke text, likes text, dislikes text)""")
con.commit()
con.close()