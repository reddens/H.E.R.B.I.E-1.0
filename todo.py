import sqlite3 # here we import the sqlite3 module
conn=sqlite3.connect("data.db") 
create_table="create table if not exists data(taskname varchar(255), taskinfo varchar(255))" #the sql statement to create a table
cur=conn.cursor()
cur.execute(create_table)
conn.commit() # finally commit the connection  to make the changes
 
def display_data():
    cur.execute("SELECT * from data")
    results=cur.fetchall()
    display=[]
    for x in results:
        display.append(x)
        return display
     
 
def create_task(taskname, taskinfo):
    insert_sql="INSERT INTO  data(taskname,taskinfo) values(?,?)"
    cur.execute(insert_sql,(taskname,taskinfo))
    conn.commit()
    print("record inserted")
 
def delete_task(taskname):
    try:
        cur.execute("DELETE FROM data WHERE taskname=?",(taskname,))
        conn.commit()
        display_data()
        print("record deleted")
    except sqlite3.Error:
        print("no task found with name ",taskname)