import sqlite3

# Db connect.
mydb = sqlite3.connect("car_wash.db")

# My cursor.
my_cursor = mydb.cursor()


#  login table  CRUD

def check_for_user_and_pass(user_name_label_get, hashed):
    """# Check a database for username and userpass."""
    query = "SELECT * FROM login WHERE username = '%s'" \
            " AND userpass = '%s'" % (user_name_label_get, hashed)

    my_cursor.execute(query)
    return my_cursor.fetchone()


def check_if_user_exist_in_database(username_info):
    """ Check if user exist in database."""
    query = "SELECT * FROM login WHERE username = '%s'" % username_info
    my_cursor.execute(query)
    return my_cursor.fetchone()


def register_user_to_database(username_info, hashed):
    """ Register user to database(insert)."""
    query = "INSERT INTO login (username, userpass) VALUES(?, ?)"
    values_user_name_user_pass = (username_info, hashed)
    my_cursor.execute(query, values_user_name_user_pass)
    mydb.commit()


#  st_material table CRUD

def add_material_to_database(get_material_id, get_thickness, get_x_size, get_y_size):
    """Add material parameters to database."""
    query = "INSERT INTO st_material (id, thickness, size_x, size_y) VALUES(?, ?, ?, ?)"
    val = (get_material_id, get_thickness, get_x_size, get_y_size)
    my_cursor.execute(query, val)
    mydb.commit()


def check_if_material_is_exist_in_database(get_material_id):
    """Check if material exist  in database"""
    query = "SELECT * FROM st_material WHERE id = '%s'" % get_material_id
    my_cursor.execute(query)
    return my_cursor.fetchone()


def select_all_material():
    """SELECT all material for showing in treeview."""
    my_cursor.execute("SELECT * FROM st_material;")
    mydb.commit()


def select_material(material_id: str) -> tuple:
    """SELECT material by ID"""
    query = f"SELECT * FROM st_material WHERE id='{material_id}';"
    my_cursor.execute(query)
    records = my_cursor.fetchall()
    return records[0] if len(records) > 0 else records


def search_material_in_database(id_variable2):
    """Search material in database where id."""
    query = f"SELECT * FROM st_material WHERE id LIKE '%{id_variable2}%'"
    my_cursor.execute(query)


def update_material(material: list):
    """Update  material."""
    material_id, thickness, size_x, size_y, in_storage, ordered, write_off = material
    query = f"UPDATE st_material  SET thickness = '{thickness}',size_x='{size_x}', size_y='{size_y}', " \
            f"in_storage='{in_storage}', ordered='{ordered}', write_off='{write_off}' WHERE id = '{material_id}'"
    my_cursor.execute(query)
    mydb.commit()


# Here have some troubles with update material in order, ordered material update only one time
# **Always need restart program for update ordered material.
def update_ordered_material(order_value, set_selection):
    """Update ordered, material."""
    query = "UPDATE st_material  SET ordered = ? WHERE id = ?"
    my_cursor.execute(query, (order_value, set_selection))


# Here have some troubles with update material in storage.
# **
def update_material_in_storage(to_storage_var, set_selection):
    """Update material in storage."""
    query = "UPDATE st_material  SET in_storage = ? WHERE id = ?"
    my_cursor.execute(query, (to_storage_var, set_selection))


def delete_material_from_database(x):
    """Function for delete material."""
    query = "DELETE FROM st_material WHERE id=?"
    my_cursor.execute(query, (x,))
    mydb.commit()


def cursor_fetch_all():
    return my_cursor.fetchall()


def create_tables():
    """Function for create tables at the start of the program."""
    query = "CREATE TABLE IF NOT EXISTS login(username VARCHAR(40), userpass VARCHAR(40))"
    my_cursor.execute(query)
    mydb.commit()
    query = "CREATE TABLE IF NOT EXISTS st_material(id VARCHAR(40), thickness INT, size_x INT," \
            " size_y INT, in_storage INT, ordered VARCHAR(40), write_off INT)"
    my_cursor.execute(query)
    mydb.commit()
