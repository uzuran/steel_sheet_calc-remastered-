import tkinter as tk
import hashlib

import Connection
import Components
import Languages


class RegisterUserScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title("Steel sheet calculator.")

        # Add username, password string line.
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        # Register window label.
        register_label = tk.Label(self, Components.registration_new_user_conf())
        register_label.pack()

        # User name label.
        user_name_label = tk.Label(self, text=Languages.current_lang["username_label"])
        user_name_label.pack()

        # Username entry.
        self.user_name_entry = tk.Entry(self, textvariable=self.user_name)
        self.user_name_entry.pack()

        # Password label.
        pass_label = tk.Label(self, text=Languages.current_lang["password_label"])
        pass_label.pack()

        # User password entry.
        self.pass_entry = tk.Entry(self, textvariable=self.password, show="*")
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
        username_info = self.user_name.get()
        password_info = self.password.get()

        if username_info.isdigit():
            Components.warning_for_registration()
            # If password have only blank on field label say it.

        elif password_info == "":
            Components.warning_for_registration()

        elif Connection.check_if_user_exist_in_database(username_info):
            Components.warning_user_exist()

        else:
            # Register user to database
            hashed = hashlib.md5(str.encode(password_info)).hexdigest()
            Connection.register_user_to_database(username_info, hashed)

            self.user_name_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)

            Components.registration_success()

