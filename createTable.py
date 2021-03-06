import mysql.connector
from mysql.connector import errorcode

try:
  # attempt to connect to database
  # enter credentials  
  db = mysql.connector.connect(user='team14', password='',
  host='35.173.239.182',
  database='bpos')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print('connected')
  cursor =  db.cursor()
  
  cursor.execute("CREATE TABLE kMeansClusteringModel ("
  + "location varchar(255),"
  + "income varchar(255),"
  + "chance varchar(255),"
  + "donation varchar(255),"
  + "locationNorm varchar(255),"
  + "salaryNorm varchar(255)"
  + ");")

  db.close()
