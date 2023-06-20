import mysql.connector

def mijnownfunction():
  mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    username="root",
    password="root",
    database="olcdb2306"
  )
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM bike")

  myresult = mycursor.fetchall()
  returnString = ""
  for x in myresult:
    returnString += x[1]

  return returnString

print(mijnownfunction())