import MySQLdb
db = MySQLdb.connect("localhost", "root", "redhat", "Database1")
a = db.cursor()
#a.execute("select * from pet;")
#a.execute(countrow)
sql = "select * from pet;"
a.execute(sql)
#countrow = a.execute(sql)
#print("Number of rows:" ,countrow)
data = a.fetchall()
print(data)

