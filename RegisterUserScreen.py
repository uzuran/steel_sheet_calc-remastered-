import tkinter as tk
import hashlib

import Connection
import Config


class RegisterUserScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title("Steel sheet calculator.")

        # Add username, password string line.
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        # Register window label.
        register_label = tk.Label(self, Config.registration_new_user_conf())
        register_label.pack()

        # User name label.
        user_name_label = tk.Label(self, text="Username")
        user_name_label.pack()

        # Username entry.
        self.user_name_entry = tk.Entry(self, textvariable=self.user_name)
        self.user_name_entry.pack()

        # Password label.
        pass_label = tk.Label(self, text="Password")
        pass_label.pack()

        # User password entry.
        self.pass_entry = tk.Entry(self, textvariable=self.password, show="*")
        self.pass_entry.pack()

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Register button.
        register_user_button = tk.Button(self, Config.registration_button())
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

        # Check if user exist in database
        Connection.check_if_user_exist_in_database(username_info)

        if username_info.isdigit():
            no_num = tk.Label(self, Config.warning_for_registration())
            no_num.pack()
            # If password have only blank on field label say it.

        elif password_info == "":
            pass_inf = tk.Label(self, Config.warning_for_registration())
            pass_inf.pack()

        elif Connection.my_cursor.fetchone():
            user_ex = tk.Label(self, Config.warning_user_exist())
            user_ex.pack()

        else:
            # Register user to database
            hashed = hashlib.md5(str.encode(password_info)).hexdigest()
            Connection.register_user_to_database(username_info, hashed)

            self.user_name_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)

            reg_success = tk.Label(self, Config.registration_success())
            reg_success.pack()
