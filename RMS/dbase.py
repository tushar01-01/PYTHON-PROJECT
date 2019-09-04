import sqlite3
db=sqlite3.connect('rms.db')
cur=db.cursor()
cur.execute("create table if not exists menulist\
(id integer primary key autoincrement,\
itemname varchar(50), price double)")
cur.execute("create table if not exists invoices\
(id integer primary key autoincrement,\
name varchar(50), mobile varchar(15), items varchar(500),\
price varchar(100), total double)")
db.commit()
