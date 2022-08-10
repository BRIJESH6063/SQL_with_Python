import mysql.connector
from mysql.connector import Error
import pandas as pd
#mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Brij@shk01" )

def create_server_connection(host_name, user_name, user_password) :
    connection = None 
    try :
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("Mysql Database connection successful") 
    except Error as err :
        print(f"Error : '{err}'")
    return connection

#   mysql password
pw = "Brij@shk01" 
#  Database Name
db = "mysql_python"

connection = create_server_connection("localhost", "root", pw)

# create mysql_python 
def create_database(connection, query) :
    cursor = connection.cursor()
    try :
        cursor.execute(query)
        print("database created successfully!")
    except Error as err :
        print(f"Error : '{err}'")
        
create_database_query = "create database mysql_python"
create_database(connection, create_database_query)