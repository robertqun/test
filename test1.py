import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('create table user (id int(11) primary key, name varchar(20))')
cursor.execute('insert into user (name) values (\'Varbo\')')
#cursor.rowcount
#cursor.execute('select * from user where id=?', (1,))
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()