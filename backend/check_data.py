import sqlite3

def fetch_latest(n=5):
    conn=sqlite3.connect('metrics.db')
    cursor=conn.cursor()
    cursor.execute('''select * from metrics order by timestamp DESC LIMIT ? ''',(n,))
    rows=cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)
        
if __name__=="__main__":
    fetch_latest()
  