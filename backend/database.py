import sqlite3

def create_connection(db_file='metrics.db'):
    conn=sqlite3.connect(db_file)
    return conn 

def create_table():
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute(""" create table if not exists metrics ( id INTEGER PRIMARY KEY AUTOINCREMENT, server_name TEXT, cpu REAL,memory REAL, disk REAL, network REAL, timestamp Text)""")
    conn.commit()
    conn.close()
    
    
if __name__=="__main__":
    create_table()
    print("table has been created!!")
    
    