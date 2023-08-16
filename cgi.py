#!C:\Users\sgaya\AppData\Local\Programs\Python\Python311\pythonw.exe "C:\Users\sgaya\AppData\Local\Programs\Python\Python311\Lib\idlelib\idle.pyw"
import cgi
import mysql.connector

print("Content-type:text/html\n")

db_connection=mysql.connector.connect(
    host='localhost',
    root='root',
    password='',
    database='mydatabase'
)

cursor=db_connection.cursor()
form=cgi.FieldStorage
name=form.getvalue('name','')
email=form.getvalue('email','')


if name and email:
    q='insert into user(name,email) values (%s,%s)'
    values=(name,email)
    cursor.execute(q,values)
    db_connection.commit()



cursor.execute("select * from user")
rows=cursor.fetchall


print("""
<html>
<head>
<title>cgi</title>
</head>
<body>
<h1>users</h1>
<form methos="post" action="text.py">
<label for="name" >Name</lable>
<input type="text" name="name" id="name">
<label for="email" >email</lable>
<input type="text" name="email" id="email">
<input type="submit" value ="add user">
</form>
<table>
<tr>
<th>id</th>
<th>name</th>
<th>email</th>
</tr>
""")

for  row in rows:
    user_id,user_name,user_email=row
    print(f"<tr><td>{user_id}</td><td>{user_name}</td><td>{user_email}</td>")

print("""
</table>
</body>
</html>
""")    



cursor.close()
db_connection.close()