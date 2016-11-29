import sqlite3


cx = sqlite3.connect("test.db")
cu=cx.cursor()
#cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")
#for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
#    cx.execute("insert into catalog values (?,?,?,?)", t)
cx.commit()

cu.execute("SELECT * FROM sqlite_master where type='table' and name='catalog'")
print(cu.fetchall())

cu.execute("SELECT * FROM sqlite_master where type='table' and name='catalog1'")
print(1111111111111111111111111111111111)
print(cu.fetchall())
print(1111111111111111111111111111111112)

cu.execute("select * from catalog")



date = cu.fetchone()
while date:
    print(date)
    date = cu.fetchone()

cu.close()
#print (cu.fetchone())
#print(cu.fetchall())

print ("11111111111")

