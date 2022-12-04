from tkinter import messagebox as msg
import tkinter as tk

import Languages


# <<<Warnings!>>>
def attribute_error_warning(frame1):
    error = msg.showwarning(title=Languages.english.get("warning_title"),
                            message=Languages.english.get("select_material_warning"),
                            parent=frame1)
    return error


def warning_msg_for_add_material_to_storage(frame1, to_storage_var):
    warning = msg.askyesno(title=Languages.english.get("warning_title"),
                           message=f"Dou you really "
                                   f"want add this {to_storage_var} count "
                                   f"of material ?",
                           parent=frame1)
    return warning


def tk_tlc_error_msg(frame1):
    tk_tlc_error = msg.showwarning(Languages.english.get("warning_title"),
                                   message=Languages.english.get("only_numbers_warning"),
                                   parent=frame1)

    return tk_tlc_error


def warning_msg_for_add_mat_to_order(frame1, order_value):
    warning = msg.askyesno(title=Languages.english.get("warning_title"),
                           message=f"Dou you really "
                                   f"want add this {order_value} count "
                                   f"of material ?",
                           parent=frame1)
    return warning


# To do here, wrong usage self! Need fix here.
def check_who_is_login(self, user_name_label_get):
    self.who_is_log_in = user_name_label_get
    check_user = tk.Label(self,
                          text=str(self.who_is_log_in).capitalize() + Languages.english.get("check_who_is_login_label"),
                          fg="green",
                          font="Arial",

                          )
    check_user.pack(anchor="e")
    return check_user


def warning_for_registration():
    """If username have some numbers msg send it on screen."""
    warning = msg.showwarning(title=Languages.english.get("warning_title"),
                              message=Languages.english.get("registration_warning"),
                              )
    return warning


def warning_user_exist():

    """If username have some numbers msg send it on screen."""
    warning = msg.showwarning(title=Languages.english.get("warning_title"),
                              message=Languages.english.get("user_exist_warning"),
                              )
    return warning


def registration_success():
    """If registration is success send it on screen."""
    success = msg.showinfo(title=Languages.english.get("Registration complete"),
                           message=Languages.english.get("registration_success"))

    return success


def warning_msg_user_not_exist():
    """Message if user not exist"""
    user_not_exist_message = msg.showwarning(title=Languages.english.get("warning_title"),
                                             message=Languages.english.get("user_not_exist_warning"))

    return user_not_exist_message


def warning_material_is_exist_msg():
    """Message if user not exist"""
    material_exist_warning = msg.showwarning(title=Languages.english.get("warning_title"),
                                             message=Languages.english.get("material_exist_warning"))

    return material_exist_warning


def warning_material_specification():
    """Warning for material specification"""
    material_specification = msg.showwarning(title=Languages.english.get("warning_title"),
                                             message=Languages.english.get("material_specification_warning"))
    return material_specification


def warning_for_delete_material(frame1):
    """Message if you want to delete material from DB"""
    delete_material_warning = msg.askyesno(title=Languages.english.get("warning_title"),
                                           message=Languages.english.get("delete_material_warning"),
                                           parent=frame1)

    return delete_material_warning


def warning_for_selecting_material(frame1):
    """Message if user not exist"""
    select_material_warning = msg.showwarning(title=Languages.english.get("warning_title"),
                                              message=Languages.english.get("select_material_warning"),
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
