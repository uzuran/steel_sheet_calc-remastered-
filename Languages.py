import configparser

# Basic configuration configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {}
configuration = config["DEFAULT"]

# Titles
configuration["main_work_title"] = "Steel sheet calculator."

# Labels
configuration["main_label"] = "Please login or register"
configuration["username_label"] = "Username"
configuration["password_label"] = "Password"
configuration["main_work_screen_label"] = "Steel sheet calculator."
configuration["check_who_is_login_label"] = "is log in now."

# Buttons
configuration["login_button"] = "Log in"
configuration["registration_button"] = "New user registration"
configuration["user_create_button"] = "Create new user"
configuration["create_new_material_button"] = "Create new material"
configuration["delete_button"] = "Delete material"
configuration["update_records_button"] = "Update records"
configuration["create_new_material_button"] = "Create new material"
configuration["add_ordered_material_button"] = "Add ordered material"
configuration["search_button"] = "Search"
configuration["add_to_storage_button"] = "Add to storage"

# Frames
configuration["frame1"] = "Steel sheet calculator."
configuration["frame2"] = "Aluminium material"
configuration["frame3"] = "Stainless material"
configuration["frame4"] = "Special material"
configuration["frame5"] = "Write off"

# Treeview
configuration["treeview_id"] = "Id:"
configuration["treeview_thickness"] = "Thickness:"
configuration["treeview_x"] = "X size:"
configuration["treeview_y"] = "Y size:"
configuration["treeview_in_storage"] = "In storage:"
configuration["treeview_order"] = "Ordered"
configuration["treeview_write_off"] = "Write off"

# Warnings
configuration["warning_title"] = "Warning!"
configuration["select_material_warning"] = "Firstly you need to select the material!"
configuration["add_mater_to_storage_warning"] = "Do you really want add this count of materia?"
configuration["only_numbers_warning"] = "You need add only numbers into entry!"
configuration["user_exist_warning"] = "User exist!"
configuration["registration_warning"] = "User name cant be empty or contain digit!"
configuration["registration_success"] = "Registration success."
configuration["user_not_exist_warning"] = "User dose not exist!"
configuration["material_exist_warning"] = "This material already exist!"
configuration["material_specification_warning"] = "You cant` add this specification of material"
configuration["delete_material_warning"] = "Are you sure that you want delete this material ?"


# <<<Languages>>>
english = {"main_work_title": "Steel sheet calculator.",
           "main_label": "Please login or register",
           "login_button": "Log in",
           "registration_button": "New user registration",
           "user_create_button": "Create new user",
           "username_label": "username",
           "password_label": "password",
           "main_work_screen_label": "Steel sheet calculator.",
           "check_who_is_login_label": "is login now.",
           "create_new_material_button": "Create new material",
           "frame1": "Steel material",
           "frame2": "Aluminium material",
           "frame3": "Stainless material",
           "frame4": "Special material",
           "frame5": "Write off",
           "treeview_id": "Id:",
           "treeview_thickness": "Thickness:",
           "treeview_x": "X size:",
           "treeview_y": "Y size:",
           "treeview_in_storage": "In storage:",
           "treeview_order": "Ordered",
           "treeview_write_off": "Write off",
           "delete_button": "Delete material",
           "update_records_button": "Update records",
           "search_button": "Search",
           "add_ordered_material_button": "Add ordered material",
           "add_to_storage_button": "Add to storage",
           "warning_title": "Warning!",
           "select_material_warning": "Firstly you need select the material!",
           "add_mater_to_storage_warning": "Do you really want add this count of materia?",
           "only_numbers_warning": "You need add only numbers into entry!",
           "user_exist_warning": "User exist!",
           "registration_warning": "You can not have a numbers, or blank line in name!",
           "registration_success": "Registration success.",
           "user_not_exist_warning": "User not exist!",
           "material_exist_warning": "This material already exist!",
           "material_specification_warning": "You cant` add this specification of material",
           "delete_material_warning": "Are you sure that you want delete this material ?"
           }
