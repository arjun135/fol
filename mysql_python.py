import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin@123"
)

print(mydb) 

