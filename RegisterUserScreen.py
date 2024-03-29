import tkinter as tk
import hashlib

import Connection
import Components
import Languages
import StartPage


class RegistrationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Add username, password string line.
        self.user_name_variable = tk.StringVar()
        self.password_variable = tk.StringVar()

        # Register window label.
        register_label = tk.Label(self, Components.registration_new_user_conf())
        register_label.pack()

        # Back to main page button.

        self.back_image = tk.PhotoImage(file="img/back.png")
        self.button_image_for_back = tk.Button(self, image=self.back_image, borderwidth=0)
        self.button_image_for_back['command'] = lambda: controller.show_frame(StartPage.StartPage)
        self.button_image_for_back.pack()

        # User name label.
        user_name_label = tk.Label(self, text=Languages.current_lang["username_label"])
        user_name_label.pack()

        # Username entry.
        self.user_name_entry = tk.Entry(self, textvariable=self.user_name_variable)
        self.user_name_entry.pack()

        # Password label.
        password_label = tk.Label(self, text=Languages.current_lang["password_label"])
        password_label.pack()

        # User password entry.
        self.pass_entry = tk.Entry(self, textvariable=self.password_variable, show="*")
        self.pass_entry.pack()

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Register button.
        register_user_button = tk.Button(self, Components.registration_button())
        # Command for button
        register_user_button['command'] = self.register_users
        register_user_button.pack()
        # Bind Enter key for entry lines.
        self.user_name_entry.bind("<Return>", self.register_users)
        self.pass_entry.bind("<Return>", self.register_users)

    def register_users(self, event=None):
        """Function for register new users, validate name without numbers,store all info in text file,
        hash password."""
        username_get = self.user_name_variable.get()
        password_get = self.password_variable.get()

        if username_get.isdigit():
            Components.warning_for_registration()
            # If password have only blank on field label say it.

        elif password_get == "":
            Components.warning_for_registration()

        elif Connection.check_if_user_exist_in_database(username_get):
            Components.warning_user_exist()

        else:
            # Register user to database
            hashed = hashlib.md5(str.encode(password_get)).hexdigest()
            Connection.register_user_to_database(username_get, hashed)

            self.user_name_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)

            Components.registration_success(self)

