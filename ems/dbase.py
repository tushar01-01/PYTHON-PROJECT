import sqlite3
db=sqlite3.connect('ems.db')
cur=db.cursor()
cur.execute("create table if not exists admin(id integer primary key autoincrement,\
name varchar(20), email varchar(50), password varchar(50))")
cur.execute("create table if not exists department(id integer primary key autoincrement, name varchar(20),\
email varchar(50))")
cur.execute("create table if not exists employee(id integer primary key autoincrement, name varchar(20),\
dob varchar(50), contact varchar(15), email varchar(50), address varchar(100), profile varchar(20),\
department integer, salary double )")
cur.execute("create table if not exists attendance(id integer primary key autoincrement, adate date,\
eid varchar(100))")
#cur.execute("insert into admin(name, email, password) values('Rajat','admin','123')")
db.commit()
