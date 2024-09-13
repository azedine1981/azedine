import psycopg2
connection = psycopg2.connect(database="azedinebase",
                             host="localhost",
                             port=5432)

cursor = connection.cursor()
cursor.execute('select \'Hello World\'')
for row in cursor:
 print(row)

cursor.close()
connection.close()
