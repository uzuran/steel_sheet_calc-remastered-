from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("English.ini", encoding="UTF-8")
conf_lang = config_object["DEFAULT"]

current_lang = dict(config_object["DEFAULT"])

# conf_lang["main_label"] = "Please login or register"
# with open('Czech.ini', 'w', encoding="utf-8") as conf:
#     config_object.write(conf)

# configuration["main_label"] = "Please login or register"
# configuration["username_label"] = "Username"
# configuration["password_label"] = "Password"
# configuration["check_who_is_login_label"] = "is log in now."
#
# # Buttons
# configuration["login_button"] = "Log in"
# configuration["registration_button"] = "New user registration"
# configuration["user_create_button"] = "Create new user"
# configuration["create_new_material_button"] = "Create new material"
# configuration["delete_button"] = "Delete material"
# configuration["update_records_button"] = "Update records"
# configuration["add_ordered_material_button"] = "Add ordered material"
# configuration["search_button"] = "Search"
# configuration["add_to_storage_button"] = "Add to storage"
#
# # Frames
# configuration["frame1"] = "Steel material."
# configuration["frame2"] = "Aluminium material"
# configuration["frame3"] = "Stainless material"
# configuration["frame4"] = "Special material"
# configuration["frame5"] = "Write off"
#
# # Treeview
# configuration["treeview_id"] = "Id:"
# configuration["treeview_thickness"] = "Thickness:"
# configuration["treeview_x"] = "X size:"
# configuration["treeview_y"] = "Y size:"
# configuration["treeview_in_storage"] = "In storage:"
# configuration["treeview_order"] = "Ordered"
# configuration["treeview_write_off"] = "Write off"
#
# # Warnings
# configuration["warning_title"] = "Warning!"
# configuration["select_material_warning"] = "Firstly you need to select the material!"
# configuration["add_mater_to_storage_warning"] = "Do you really want add this count of materia?"
# configuration["only_numbers_warning"] = "You need add only numbers into entry!"
# configuration["user_exist_warning"] = "User exist!"
# configuration["registration_warning"] = "User name cant be empty or contain digit!"
# configuration["registration_success"] = "Registration success."
# configuration["user_not_exist_warning"] = "User dose not exist!"
# configuration["material_exist_warning"] = "This material already exist!"
# configuration["material_specification_warning"] = "You cant` add this specification of material"
# configuration["delete_material_warning"] = "Are you sure that you want delete this material?"
#
# with open('English.ini', 'w') as conf:
#     config.write(conf)

# # Basic configuration configparser
# config_cz = configparser.ConfigParser()
# config_cz["DEFAULT"] = {}
# configuration = config_cz["DEFAULT"]
#
# # Titles
# configuration["main_work_title"] = "Kalkul??ka na plechy "
#
# # Labels
# configuration["main_label"] = "P??ihlaste se pros??m nebo se zaregistrujte!"
# configuration["username_label"] = "U??ivatelsk?? jm??no"
# configuration["password_label"] = "Helso"
# configuration["main_work_screen_label"] = "Odpis plech??."
# configuration["check_who_is_login_label"] = "je  p??ihl????en??."
#
# # Buttons
# configuration["login_button"] = "P??ihl??sit se"
# configuration["registration_button"] = "Registrace"
# configuration["user_create_button"] = "Registrace nov??ho u??ivatele"
# configuration["create_new_material_button"] = "Vytvo??it nov?? materi??l"
# configuration["delete_button"] = "Odstranit materi??l"
# configuration["update_records_button"] = "Obnovit z??pis"
# configuration["add_ordered_material_button"] = "P??idat objednan?? materi??l"
# configuration["search_button"] = "Vyhledat materi??l"
# configuration["add_to_storage_button"] = "P??idat materi??l do skladu"
#
# # Frames
# configuration["frame1"] = "??elezo"
# configuration["frame2"] = "Hlin??k"
# configuration["frame3"] = "Nerez"
# configuration["frame4"] = "Speci??ln?? materi??l"
# configuration["frame5"] = "Odpis materi??l??"
#
# # Treeview
# configuration["treeview_id"] = "Id:"
# configuration["treeview_thickness"] = "Tlou????ka:"
# configuration["treeview_x"] = "X size:"
# configuration["treeview_y"] = "Y size:"
# configuration["treeview_in_storage"] = "Ve sklad??:"
# configuration["treeview_order"] = "Objednan?? materi??l"
# configuration["treeview_write_off"] = "Odepsan?? materi??l"
#
# # Warnings
# configuration["warning_title"] = "Upozorn??n??"
# configuration["select_material_warning"] = "Nejprve mus??te  zvolit materi??l !"
# configuration["add_mater_to_storage_warning"] = "Opravdu chcete p??idat takove mno??stv?? materi??l???"
# configuration["only_numbers_warning"] = "Povolen?? jsou jen ????slice!"
# configuration["user_exist_warning"] = "U??ivatel existuje!"
# configuration["registration_warning"] = "U??ivatelsk?? jm??no nesm?? b??t pr??zdn?? nebo obsahovat ????slice!"
# configuration["registration_success"] = "Registrace prob??hla ??sp????n??."
# configuration["user_not_exist_warning"] = "U??ivatel neexistuje!"
# configuration["material_exist_warning"] = "Tento materi??l ji?? existuje."
# configuration["material_specification_warning"] = "Nem????ete p??idat materi??l t??to specifikace.."
# configuration["delete_material_warning"] = "Opravdu chcete odstranit tento materi??l?"
#

