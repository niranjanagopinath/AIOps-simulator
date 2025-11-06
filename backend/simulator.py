import random
import sqlite3
import  datetime
import time 


DB_FILE="metrics.db"

def insert_metric(server_name,cpu,memory,disk,network,timestamp):
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute(''' insert into metrics(server_name,cpu,memory,disk,network,timestamp)
                   values(?,?,?,?,?,?)''',(server_name,cpu,memory,disk,network,timestamp))
    conn.commit()
    conn.close()
    
def simulate_metrics():
    server_list=["server-1","server-2","server-3"]
    while True:
        for server in server_list:
            cpu=round(random.uniform(10,90),2)
            memory = round(random.uniform(20, 95), 2)
            disk = round(random.uniform(10, 80), 2)
            network = round(random.uniform(0.1, 2.0), 2)
            timestamp = datetime.datetime.now().isoformat()
            
            insert_metric(server,cpu,memory,disk,network,timestamp)
            print("inserted!")
        time.sleep(5)

if __name__=="__main__":
    simulate_metrics()
        
    