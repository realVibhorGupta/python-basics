import sqlite3

'''this the line d=fror database connectivity'''
conn = sqlite3.connect("E:\Projects\PythonLearning\sql1.db")
# here full path comes and username,password etc
cursor = conn.cursor()

cursor.execute(

    "SELECT * FROM Track"
)
result = cursor.fetchall()
# it gives lists
print result
conn.close()
