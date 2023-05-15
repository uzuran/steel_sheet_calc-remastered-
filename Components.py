from tkinter import messagebox as msg
import tkinter as tk

import Languages
from Config import *


# <<<Warnings!>>>
def attribute_error_warning(frame1):
    error = msg.showwarning(title=Languages.current_lang["warning_title"],
                            message=Languages.current_lang["select_material_warning"],
                            parent=frame1)
    return error


def only_numbers_is_allowed_warning(frame1):
    only_numbers_is_allowed = msg.showwarning(title=Languages.current_lang["warning_title"],
                                              message=Languages.current_lang["only_numbers_warning"],
                                              parent=frame1)
    return only_numbers_is_allowed


def warning_message_write_off_is_bigger_then_mat_in_storage(frame1):
    write_off_warning = msg.showwarning(title=Languages.current_lang["warning_title"],
                                        message=Languages.current_lang["warning_message_write_off_is_"
                                                                       "bigger_then_mat_in_storage"],
                                        parent=frame1)
    return write_off_warning


def warning_msg_for_add_material_to_storage(frame1):
    warning = msg.askyesno(title=Languages.current_lang["warning_title"],
                           message=Languages.current_lang["warning_message_add_material"],
                           parent=frame1)
    return warning


def tk_tlc_error_msg(frame1):
    tk_tlc_error = msg.showwarning(Languages.current_lang["warning_title"],
                                   message=Languages.current_lang["only_numbers_warning"],
                                   parent=frame1)

    return tk_tlc_error


def warning_msg_for_add_mat_to_order(frame1):
    warning = msg.askyesno(title=Languages.current_lang["warning_title"],
                           message=Languages.current_lang["warning_message_add_material"],
                           parent=frame1)
    return warning


# To do here, wrong usage self! Need fix here.
def check_who_is_login(self, user_name_label_get):
    self.who_is_log_in = user_name_label_get
    check_user = tk.Label(self,
                          text=str(self.who_is_log_in).capitalize() + " "
                          + Languages.current_lang["check_who_is_login_label"],
                          fg=conf["colour_green"],
                          font=conf["font"],

                          )
    check_user.pack(anchor="e")
    return check_user


def warning_for_registration():
    """If username have some numbers msg send it on screen."""
    warning = msg.showwarning(title=Languages.current_lang["warning_title"],
                              message=Languages.current_lang["registration_warning"],
                              )
    return warning


def warning_user_exist():

    """If username have some numbers msg send it on screen."""
    warning = msg.showwarning(title=Languages.current_lang["warning_title"],
                              message=Languages.current_lang['user_exist_warning'],
                              )
    return warning


def registration_success(self):
    """If registration is success send it on screen."""
    success = msg.showinfo(title=Languages.current_lang["registration_success"],
                           message=Languages.current_lang["registration_success"],
                           parent=self)

    return success


def warning_msg_user_not_exist():
    """Message if user not exist"""
    user_not_exist_message = msg.showwarning(title=Languages.current_lang["warning_title"],
                                             message=Languages.current_lang["user_not_exist_warning"])

    return user_not_exist_message


def warning_material_is_exist_msg():
    """Message if user not exist"""
    material_exist_warning = msg.showwarning(title=Languages.current_lang["warning_title"],
                                             message=Languages.current_lang["material_exist_warning"])

    return material_exist_warning


def warning_material_specification():
    """Warning for material specification"""
    material_specification = msg.showwarning(title=Languages.current_lang["warning_title"],
                                             message=Languages.current_lang["material_specification_warning"])
    return material_specification


def warning_for_delete_material(frame1):
    """Message if you want to delete material from DB"""
    delete_material_warning = msg.askyesno(title=Languages.current_lang["warning_title"],
                                           message=Languages.current_lang["delete_material_warning"],
                                           parent=frame1)

    return delete_material_warning


def warning_for_selecting_material(frame1):
    """Message if user not exist"""
    select_material_warning = msg.showwarning(title=Languages.current_lang["warning_title"],
                                              message=Languages.current_lang["select_material_warning"],
                                              parent=frame1)

    return select_material_warning


# <<<BUTTONS>>>
def add_material_to_storage_button():
    add_mat_to_storage_button = {"text": Languages.current_lang["add_to_storage_button"]}

    return add_mat_to_storage_button


def add_to_order_button():
    add_mat_button = {"text":  Languages.current_lang["add_ordered_material_button"]}

    return add_mat_button


def search_button():
    search_button = {"text": Languages.current_lang["search_button"]}

    return search_button


def update_records_button():
    delete_button = {"text": Languages.current_lang["update_records_button"]}

    return delete_button


def delete_material_button():
    delete_button = {"text": Languages.current_lang["delete_button"]}

    return delete_button


def main_button_conf_login():
    """"Button for login, config."""
    log_in = {"text": Languages.current_lang["login_button"],
              "width": conf["main_button_width"],
              "height": conf["main_button_height"]
              }
    return log_in


def main_button_conf_registration():
    """Button for registration config."""
    registration_new_user_button = {"text": Languages.current_lang["registration_button"],
                                    "width": conf["main_button_width"],
                                    "height": conf["main_button_height"]
                                    }

    return registration_new_user_button


def registration_button():
    """Button for registration config."""
    registration = {
        "text": Languages.current_lang["user_create_button"],
        "width": conf["lr_button_width"],
        "height": conf["lr_button_height"]
    }

    return registration


def login_button():
    """Button for login config."""
    button_for_login = {"text": Languages.current_lang["login_button"],
                        "width": conf["lr_button_width"],
                        "height": conf["lr_button_height"]
                        }

    return button_for_login


def create_new_material_button():
    """Button for create material config."""
    create_new_mat_button = {"text": Languages.current_lang["create_new_material_button"]}

    return create_new_mat_button


# <<<LABELS>>>
def main_label_conf():
    """Configurate , text, background, width, height, font for main label."""
    label = {"text": Languages.current_lang["main_label"],
             "bg": conf["main_background"],
             "width": conf["main_label_width"],
             "height": conf["main_label_height"],
             "font": conf["font"]}
    return label


def label_for_option_screen():
    """Configurate , text, background, width, height, font for option screen label."""
    label = {"text": Languages.current_lang["choice_your_lang"],
             "bg": conf["main_background"],
             "width": conf["main_label_width"],
             "height": conf["main_label_height"],
             "font": conf["font"]}
    return label


def registration_new_user_conf():
    """Configurate , text, background, width, height, font for registration user."""
    label = {"text": Languages.current_lang["registration_label"],
             "bg": conf["main_background"],
             "width": conf["main_label_width"],
             "height": conf["main_label_height"],
             "font": conf["font"]}
    return label


def login_user_conf():
    """Configurate , text, background, width, height, font for login user."""
    label = {"text": Languages.current_lang["main_label"],
             "bg": conf["main_background"],
             "width": conf["main_label_width"],
             "height": conf["main_label_height"],
             "font": conf["font"]}

    return label


def admin_label_conf():
    """Configurate , text, background, width, height, font for admin screen."""
    label = {"text": Languages.current_lang["main_work_label"],
             "bg":  conf["main_background"],
             "width": conf["main_label_width"],
             "height": conf["main_label_height"],
             "font": conf["font"]}

    return label


def create_new_material_label():
    """Configurate , text, background, width, height, font for create new material."""
    label = {"text": Languages.current_lang["create_new_material_button"],
             "bg":  conf["main_background"],
             "width": conf["main_label_width"],
             "height": conf["main_label_height"],
             "font": conf["font"]}

    return label


def option_for_labels():
    option = {"padx": conf["option_for_labels"],
              "pady": conf["option_for_labels"]}

    return option


def option_for_size_frame():
    frame_options = {"width": conf["frame_width"],
                     "height": conf["frame_height"]}

    return frame_options


