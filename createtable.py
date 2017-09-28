#import MySQLdb
#db = MySQLdb.connect("localhost", "root", "redhat", "Database1")
#a = db.cursor()
#a.execute("Drop Table if exists EMPLOYEE")
#sql = """create table EMPLOYEE (firstname CHAR(20) NOT NULL, lastname char(20), AGE INT, Income FLOAT)"""
#a.execute(sql)
#db.close()


#import MySQLdb
#db = MySQLdb.connect("localhost", "root", "redhat", "Database1")
#a = db.cursor()
#sql = """INSERT INTO EMPLOYEE (firstname, lastname, AGE, Income) VALUES ('prabhas', 'uppalapati', '35', '10000000')"""
#try:
# a.execute(sql)
#except:
# db.rollback()
#db.close()

import MySQLdb
db = MySQLdb.connect('localhost', 'root', 'redhat', 'Database1')
a = db.cursor()
a.execute("Drop Table if exists Details") 
sql = """create table Records (firstname CHAR(20), lastname char(20), age int, Location char(20))"""
a.execute(sql)
a.execute("""INSERT INTO Details (firstname, lastname, age, location) VALUES ('new', 'new1', '22', 'newyork')""")
db.close()
