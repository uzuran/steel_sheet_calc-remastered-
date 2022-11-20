import mysql.connector


# Db connect.
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database="users_data")

# My cursor.
my_cursor = mydb.cursor(buffered=True)


def check_for_user_and_pass(user_name_label_get, hashed):
    """# Check a database for username and userpass."""
    query = "SELECT * FROM login WHERE BINARY username = '%s'" \
            " AND BINARY userpass = '%s'" % (user_name_label_get, hashed)

    my_cursor.execute(query)


def check_if_user_exist_in_database(username_info):
    """ Check if user exist in database."""
    query = "SELECT * FROM login WHERE username = '%s'" % username_info
    my_cursor.execute(query)


def register_user_to_database(username_info, hashed):
    """ Register user to database(insert)."""
    query = "INSERT INTO login (username, userpass) VALUES(%s, %s)"
    values_user_name_user_pass = (username_info, hashed)
    my_cursor.execute(query, values_user_name_user_pass)
    mydb.commit()


def check_if_material_is_exist_in_database(get_material_id):
    """Check if material exist  in database"""
    query = "SELECT * FROM st_material WHERE id = '%s'" % get_material_id
    my_cursor.execute(query)


def add_material_to_database(get_material_id, get_thickness, get_x_size, get_y_size):
    """Add material parameters to database."""
    query = "INSERT INTO st_material (id, thickness, size_x, size_y) VALUES(%s, %s, %s, %s)"
    val = (get_material_id, get_thickness, get_x_size, get_y_size)
    my_cursor.execute(query, val)
    mydb.commit()


def select_all_material():
    """SELECT all material for showing in treeview."""
    my_cursor.execute("SELECT * FROM st_material;")
    mydb.commit()


def delete_material_from_database(x):
    """Function for delete material."""
    query = "DELETE FROM st_material WHERE id=%s"
    cursor = mydb.cursor()
    cursor.execute(query, (x,))
    mydb.commit()


def search_material_in_database(id_variable2):
    """Search material in database where id."""
    query = f"SELECT * FROM st_material WHERE id LIKE '%{id_variable2}%'"
    my_cursor.execute(query)


def update_ordered_material(order_value, item):
    """Update ordered, material."""
    query = "UPDATE st_material  SET ordered = %s WHERE id = %s"
    my_cursor.execute(query, (order_value, item["values"][0]))


def update_material_in_storage(to_storage_var, item):
    """Update material in storage."""
    query = "UPDATE st_material  SET in_storage = %s WHERE id = %s"
    my_cursor.execute(query, (to_storage_var, item["values"][0]))
