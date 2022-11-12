import tkinter as tk
from tkinter import *
import mysql.connector
import hashlib


mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database='users_data')

my_cursor = mydb.cursor(buffered=True)

class RegisterUserScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title("Steel sheet calculator.")

        # Global
        global user_name
        global password
        global user_name_entry
        global pass_entry

        # Add username, password string line.
        user_name = StringVar()
        password = StringVar()

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
        user_n = Label(self, text="Username")
        user_n.pack()

        # Username entry.
        user_name_entry = Entry(self, textvariable=user_name)
        user_name_entry.pack()

        # Password label.
        pass_label = Label(self, text="Password")
        pass_label.pack()

        # User password entry.
        pass_entry = Entry(self, textvariable=password, show="*")
        pass_entry.pack()

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
        user_name_entry.bind("<Return>", self.register_users)
        pass_entry.bind("<Return>", self.register_users)

    def register_users(self, event=None):
        """Function for register new users, validate name without numbers,store all info in text file,
        hash password."""
        username_info = user_name.get()
        password_info = password.get()

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
            val = (username_info, hashed)
            my_cursor.execute(sql, val)
            mydb.commit()

            user_name_entry.delete(0, END)
            pass_entry.delete(0, END)

            # Label option
            success_option = {"text": "Registration success.",
                              "fg": "green",
                              "font": "Calibri, 11"}

            reg_success = Label(self, success_option)
            reg_success.pack()
