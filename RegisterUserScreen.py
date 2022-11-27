import tkinter as tk
import hashlib

import Connection


class RegisterUserScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title("Steel sheet calculator.")

        # Add username, password string line.
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        # Register options.
        register_label_option = {
            "text": "Please enter your name and password.",
            "bg": "#d1dffa",
            "width": "300",
            "height": "2",
            "font": "Calibri, 12"
        }

        # Register window label.
        register_label = tk.Label(self, **register_label_option)
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

        register_btn_option = {
            "text": "Register",
            "width": "10",
            "height": "1"
        }

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Register button.
        register_user_button = tk.Button(self, **register_btn_option)
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

        # If username have some numbers label send it on screen.
        options = {"text": "You can not have a numbers, or blank line in name!",
                   "fg": "red",
                   "font": "Calibri, 12"}

        # Check if user exist in database
        Connection.check_if_user_exist_in_database(username_info)

        if username_info.isdigit():
            no_num = tk.Label(self, **options)
            no_num.pack()
            # If password have only blank on field label say it.

        elif password_info == "":
            pass_inf = tk.Label(self, **options)
            pass_inf.pack()

        elif Connection.my_cursor.fetchone():
            user_ex = tk.Label(self, text="User exist", fg="red", font="Calibri, 12")
            user_ex.pack()

        else:
            # Register user to database
            hashed = hashlib.md5(str.encode(password_info)).hexdigest()
            Connection.register_user_to_database(username_info, hashed)

            self.user_name_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)

            # Label option
            success_option = {"text": "Registration success.",
                              "fg": "green",
                              "font": "Calibri, 11"}

            reg_success = tk.Label(self, success_option)
            reg_success.pack()
