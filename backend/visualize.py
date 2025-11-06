import sqlite3
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import os

db="metrics.db"

def fetch_data():
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute("select timestamp, cpu,memory from metrics order by timestamp desc limit 50")
    rows=cursor.fetchall()
    conn.close()
    return rows[::-1]
    
def animate(i):
    data=fetch_data()
    if not data:
        return 
    
    timestamps=[r[0] for r in data]
    cpu=[r[1] for r in data]
    mem=[r[2]for r in data]

    plt.cla()
    plt.plot(timestamps,cpu,label="cpu usage")
    plt.plot(timestamps,mem,label="memory usage")
    plt.xlabel("timestamp")
    plt.ylabel("usage")
    plt.title("system metrics live updates")
    plt.legend()
    plt.tight_layout()
    
fig=plt.figure()
ani=animation.FuncAnimation(fig,animate,interval=2000)
plt.show()
    