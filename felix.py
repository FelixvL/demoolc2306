import mysql.connector

def mijnownfunction():
  mysql.connector.connect(
    host="localhost",
    port="8889",
    username="root",
    password="root",
    database="olcdb2306"
  )
  return "this is from felix"

mijnownfunction()