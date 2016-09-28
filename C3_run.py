from flask import Flask,render_template
import pyodbc

#create connect session
conn = pyodbc.connect('DRIVER={SQL Server};SERVER="your server or ip";DATABASE="Database name";UID="user name";PWD="password"')

app  = Flask(__name__)

#connect to sql server and  ,parameter tb_name=>giving your sql server table name
def db_fetch(tb_name):
    cursor = conn.cursor()
    cursor= conn.cursor()
    cursor.execute("select * from %s"%tb_name)
    rows = cursor.fetchall()

    return (list(rows))


@app.route('/')
def index():
    data1=  []
    data2 = []
    for a,b in db_fetch('C3'):
        data1.append(a)
        data2.append(b)
    return render_template('index.html',data1 = data1,data2 =data2)

app.run()
