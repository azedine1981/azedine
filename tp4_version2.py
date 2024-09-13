import sqlite3
conn=sqlite3.connect("abase.db")
cur=conn.cursor()
colonnes=cur.execute('SELECT * FROM t1').fetchall()
for i in colonnes:
    print(i)
conn.commit()
conn.close()
