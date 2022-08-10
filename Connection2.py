import mysql.connector
from mysql.connector import Error
import pandas as pd
import IPython
from IPython.display import display

# connect to database

#   mysql password
pw = "Brij@shk01" 
#  Database Name
db = "mysql_python"

def create_db_connection(host_name, user_name, user_password, db_name) :
    connection = None
    try :
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL database connection successful!")
    except Error as err :
        print(f"Error : '{err}'")
    return connection

# Execute mysql query 

def execute_query(connection, query) :
    cursor = connection.cursor()
    try :
        cursor.execute(query)
        connection.commit()
        print("OK! Query executed successfully!")
    except Error as err :
        print(f"Error : '{err}'")


create_orders_table = """
create table orders(
    order_id int primary key,
    customer_name varchar(30) not null,
    product_name varchar(30) not null,
    date_ordered date,
    quantity int,
    unit_price float,
    phone_number varchar(20)
) ;
"""
# connect to database 
connection = create_db_connection("localhost", "root", pw, db)

execute_query(connection, create_orders_table) 

data_orders = """
insert into orders values
(101, "Brijesh", "Laptop", '2022-08-08', 2, 42000, '7246987421'),
(102, "Ratnesh", "Trouser", '2022-09-17', 4, 426, '7246227421'),
(103, "Shivam", "T-Shirt", '2022-09-22', 5, 455, '7277987421'),
(104, "Raghav", "Headphone", '2022-11-18', 3, 1500, '7246988421'),
(105, "Rohit", "Smart-TV", '2022-11-26', 1, 4000, '7246997421') ;
"""

execute_query(connection, data_orders)

def read_query(connection, query) :
    cursor = connection.cursor()
    result = None
    try :
        cursor.execute(query)
        result = cursor.fetchall()
        return result 
    except Error as err :
        print(f"Error : '{err}'")

# query using select statement 
connection = create_db_connection("localhost", "root", pw, db)
query = input("Input select query to fetch : ")
results = read_query(connection, query)

database = []

for result in results :
    result = list(result)
    database.append(result)

columns = ["order_id", "customer_name", "product_name", "date_ordered date", "quantity", 
          "unit_price float", "phone_number"]
print("----------------------------------------------------------------------------------")
df = pd.DataFrame(database, columns = columns)
display(df)

update = input("input an update query : ")
execute_query(connection, update) 

connection = create_db_connection("localhost", "root", pw, db)
query = input("Input select query to fetch : ")
results = read_query(connection, query)

database = []

for result in results :
    result = list(result)
    database.append(result)

columns = ["order_id", "customer_name", "product_name", "date_ordered date", "quantity", 
          "unit_price float", "phone_number"]
print("----------------------------------------------------------------------------------")
df = pd.DataFrame(database, columns = columns)
display(df)

delete = input("Input delete query : ") 

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, delete) 

results = read_query(connection, query)

database = []

for result in results :
    result = list(result)
    database.append(result)

columns = ["order_id", "customer_name", "product_name", "date_ordered date", "quantity", 
          "unit_price float", "phone_number"]
print("----------------------------------------------------------------------------------")
df = pd.DataFrame(database, columns = columns)
display(df)

