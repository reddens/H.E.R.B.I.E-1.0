import sqlite3
conn = sqlite3.connect("test.db")
print("Database created")
conn.execute('''CREATE TABLE USER
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);''')
print ("Table created successfully")

conn.close()