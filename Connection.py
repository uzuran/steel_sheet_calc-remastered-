import mysql.connector


# Db connect.
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database="users_data")
