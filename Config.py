from tkinter import messagebox as msg


# <<<Warnings!>>>
def warning_for_registration():
    """If username have some numbers label send it on screen."""
    warnings = {"text": "You can not have a numbers, or blank line in name!",
                "fg": "red",
                "font": "Calibri, 12"}

    return warnings


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