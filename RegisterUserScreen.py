import tkinter as tk
from tkinter import *
import hashlib
from Connection import *


my_cursor = mydb.cursor(buffered=True)


class RegisterUserScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title("Steel sheet calculator.")

        # Add username, password string line.
        self.user_name = StringVar()
        self.password = StringVar()

        # Register options.
        register_label_option = {
            "text": "Please enter your name and password.",
            "bg": "#d1dffa",
            "width": "300",
            "height": "2",
            "font": "Calibri, 12"
        }

        # Register window label.
        register_label = Label(self, **register_label_option)
        register_label.pack()

        # User name label.
        user_name_label = Label(self, text="Username")
        user_name_label.pack()

        # Username entry.
        self.user_name_entry = Entry(self, textvariable=self.user_name)
        self.user_name_entry.pack()

        # Password label.
        pass_label = Label(self, text="Password")
        pass_label.pack()

        # User password entry.
        self.pass_entry = Entry(self, textvariable=self.password, show="*")
        self.pass_entry.pack()

        register_btn_option = {
            "text": "Register",
            "width": "10",
            "height": "1"
        }

        empty_space = Label(self, text="")
        empty_space.pack()

        # Register button.
        register_user_button = Button(self, **register_btn_option)
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

        sql = "SELECT * FROM login WHERE username = '%s'" % username_info
        my_cursor.execute(sql)

        if username_info.isdigit():
            no_num = Label(self, **options)
            no_num.pack()
            # If password have only blank on field label say it.

        elif password_info == "":
            pass_inf = Label(self, **options)
            pass_inf.pack()

        elif my_cursor.fetchone():
            user_ex = Label(self, text="User exist", fg="red", font="Calibri, 12")
            user_ex.pack()

        else:
            hashed = hashlib.md5(str.encode(password_info)).hexdigest()
            sql = "INSERT INTO login (username, userpass) VALUES(%s, %s)"
            values = (username_info, hashed)
            my_cursor.execute(sql, values)
            mydb.commit()

            self.user_name_entry.delete(0, END)
            self.pass_entry.delete(0, END)

            # Label option
            success_option = {"text": "Registration success.",
                              "fg": "green",
                              "font": "Calibri, 11"}

            reg_success = Label(self, success_option)
            reg_success.pack()
