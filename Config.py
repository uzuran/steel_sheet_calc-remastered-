from tkinter import messagebox as msg
import tkinter as tk


# <<<Warnings!>>>
def attribute_error_warning(frame1):
    error = msg.showwarning(title="WARNING", message="Firstly you need select the material !",
                            parent=frame1)
    return error


def warning_msg_for_add_material_to_storage(frame1, to_storage_var):
    warning = msg.askyesno(title="Warning", message=f"Dou you really "
                                 f"want add this {to_storage_var} count "
                                 f"of material ?",
                           parent=frame1)
    return warning


def tk_tlc_error_msg(frame1):
    tk_tlc_error = msg.showwarning(title="WARNING", message="You need add only numbers into entry !",
                                   parent=frame1)

    return tk_tlc_error


def warning_msg_for_add_mat_to_order(frame1, order_value):
    warning = msg.askyesno(title="Warning", message=f"Dou you really "
                                 f"want add this {order_value} count "
                                 f"of material ?",
                           parent=frame1)
    return warning


def check_who_is_login(self, user_name_label_get):
    self.who_is_log_in = user_name_label_get
    check_user = tk.Label(self, text=str(self.who_is_log_in).capitalize() + " Is log in now.",
                          fg="green",
                          font="Arial",

                          )
    check_user.pack(anchor="e")
    return check_user


def warning_for_registration():
    """If username have some numbers label send it on screen."""
    warning = {"text": "You can not have a numbers, or blank line in name!",
                "fg": "red",
                "font": "Calibri, 12"}

    return warning


def warning_user_exist():
    """If username exist send it on screen."""
    user_exist = {"text": "User exist!",
                  "fg": "red",
                  "font": "Calibri, 12"}

    return user_exist


def registration_success():
    """If registration is success send it on screen."""
    success = {"text": "Registration success.",
                       "fg": "green",
                       "font": "Calibri, 11"}

    return success


def warning_msg_user_not_exist():
    """Message if user not exist"""
    user_not_exist_message = msg.showwarning(title="Warning", message="Warning user not exist!")

    return user_not_exist_message


def warning_material_is_exist_msg(self):
    """Message if user not exist"""
    material_exist_warning = msg.showwarning(title="Warning!", message="This material already exist!",
                                             parent=self)

    return material_exist_warning


def warning_material_specification(self):
    """Warning for material specification"""
    material_specification = msg.showwarning(title="Warning!", message="You cant add this specification of material.",
                                             parent=self)

    return material_specification


def warning_for_delete_material(frame1):
    """Message if you want to delete material from DB"""
    delete_material_warning = msg.askyesno(title="Warning !", message="Are you sure"
                                                                      " that you want delete this material ?",
                                           parent=frame1)

    return delete_material_warning


def warning_for_selecting_material(frame1):
    """Message if user not exist"""
    select_material_warning = msg.showwarning(title="WARNING", message="Firstly you need select the material !",
                                              parent=frame1)

    return select_material_warning


# <<<BUTTONS>>>
def add_material_to_storage_button():
    add_mat_to_storage_button = {"text": "Add to storage"}

    return add_mat_to_storage_button


def add_to_order_button():
    add_mat_button = {"text": "Add ordered material"}

    return add_mat_button


def search_button():
    search_button = {"text": "Search"}

    return search_button


def update_records_button():
    delete_button = {"text": "Update records"}

    return delete_button


def delete_material_button():
    delete_button = {"text": "Delete material"}

    return delete_button


def main_button_conf_login():
    """"Button for login, config."""
    log_in = {"text": "Log in",
                      "width": "30",
                      "height": "2"
              }
    return log_in


def main_button_conf_registration():
    """Button for registration config."""
    registration_new_user_button = {"text": "New user registration",
                                    "width": "30",
                                    "height": "2"
                                    }

    return registration_new_user_button


def registration_button():
    """Button for registration config."""
    registration = {
        "text": "Create new user",
        "width": "15",
        "height": "2"
    }

    return registration


def login_button():
    """Button for login config."""
    button_for_login = {"text": "Login",
                        "width": "15",
                        "height": "2",
                        }

    return button_for_login


def create_new_material_button():
    """Button for create material config."""
    create_new_mat_button = {"text": "Create new material"}

    return create_new_mat_button


# <<<LABELS>>>
def main_label_conf():
    """Configurate , text, background, width, height, font for main label."""
    label = {"text": "Please login, or register.",
                     "bg": "#d1dffa",
                     "width": "300",
                     "height": "2",
                     "font": "Calibri, 12"}
    return label


def registration_new_user_conf():
    """Configurate , text, background, width, height, font for registration user."""
    label = {"text": "Please login, or register.",
                     "bg": "#d1dffa",
                     "width": "300",
                     "height": "2",
                     "font": "Calibri, 12"}
    return label


def login_user_conf():
    """Configurate , text, background, width, height, font for login user."""
    label = {"text": "Please login, or register",
                     "bg": "#d1dffa",
                     "width": "300",
                     "height": "2",
                     "font": "Calibri, 13"}

    return label


def admin_label_conf():
    """Configurate , text, background, width, height, font for admin screen."""
    label = {"text": "Steel sheet calculator",
                    "bg": "#d1dffa",
                    "width": "300",
                    "height": "2",
                    "font": "Calibri, 13"}

    return label


def create_new_material_label():
    """Configurate , text, background, width, height, font for create new material."""
    label = {"text": "Create new material.",
             "bg": "#d1dffa",
             "width": "300",
             "height": "2",
             "font": "Calibri, 12"
             }

    return label


def option_for_labels():
    option = {"padx": 5,
              "pady": 5}

    return option
