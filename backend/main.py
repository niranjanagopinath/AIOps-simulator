from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3,os

app=FastAPI()

base_dir=os.path.dirname(__file__)
DB_PATH = "C:\\Users\\niran\\OneDrive\\Desktop\\AIOps\\metrics.db"
templates=Jinja2Templates(directory=os.path.join(base_dir,"templates"))

app.mount("/static",StaticFiles(directory=os.path.join(base_dir,"static")))


@app.get("/",response_class=HTMLResponse)
async def dashboard(request:Request):
    return templates.TemplateResponse("dashboard.html",{"request":request})

@app.get("/metrics/latest")
async def get_latest_metrics(limit:int=50):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute("select timestamp,cpu,memory from metrics order by timestamp desc limit ?",(limit,))
    rows=cursor.fetchall()
    conn.close()
    return {"data":rows[::-1]}
    
