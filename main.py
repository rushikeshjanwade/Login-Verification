from flask import Flask,render_template,request,url_for,redirect
import sqlite3
from datetime import datetime


app=Flask(__name__)

data=[]

@app.route("/")
def login_page():
    return render_template("index.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/checkentry",methods=["GET","POST"])
def check():
    username=request.form["username"]
    password=request.form["password"]
    conection = sqlite3.connect("logindetails.db")
    c = conection.cursor()
    c.execute(f"select password from logindetails where reg_id='{username}'")
    db_password=c.fetchone()
    if db_password!= None:
        if password==db_password[0]:
            conection.close()
            now = datetime.now()
            ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
            data.append(username)
            data.append(password)
            data.append(dt_string)
            data.append(ip_addr)
            append_in_logintable(data)
            data.clear()
            return redirect(url_for('home_page'))

        else:
            conection.close()
            return redirect(url_for('login_page'))
    else:
        return redirect(url_for('login_page'))

def append_in_logintable(data):
    conection = sqlite3.connect("logindetails.db")
    c = conection.cursor()
    c.execute(f"insert into logindetails values('{data[0]}','{data[1]}','{data[2]}','{data[3]}')")
    conection.commit()

if __name__=="__main__":
    app.run(debug=True)
