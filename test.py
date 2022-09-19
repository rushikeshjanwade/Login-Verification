import sqlite3

conection=sqlite3.connect("logindetails.db")

c=conection.cursor()

# query="Create table if not exists logindetails (reg_id text, password text,created_datetime text,ip text)"
#
# c.execute(query)
# conection.commit()


# c.execute("insert into logindetails values('rushi','rushi','16-09-2022 23:56','11.11.11')")
# c.execute("insert into logindetails values('yash','yash','16-09-2022 23:57','11.11.12')")
# c.execute("insert into logindetails values('pranav','pranav','16-09-2022 23:58','11.21.11')")
# c.execute("insert into logindetails values('vaibhav','vaibhav','16-09-2022 23:59','14.11.11')")
# conection.commit()

c.execute("select * from logindetails")
a=c.fetchall()
for i in a:
    print(i)