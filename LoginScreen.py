import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox as msg
import hashlib
from AdminScreen import AdminScreen
from Connection import *


my_cursor = mydb.cursor(buffered=True)


class LoginScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.title("Please login!")
        self.geometry("350x450")

        login_l_option = {"text": "Please login, or register",
                          "bg": "#d1dffa",
                          "width": "300",
                          "height": "2",
                          "font": "Calibri, 13"}
        # Main label.
        login_label = Label(self, **login_l_option)
        login_label.pack()

        global user_name_verify
        global user_pass_verify
        global user_name_entry1
        global user_pass_entry2

        user_name_verify = StringVar()
        user_pass_verify = StringVar()

        # Username label
        Label(self, text="Username").pack()

        # Username entry.
        user_name_entry1 = Entry(self, textvariable=user_name_verify)
        user_name_entry1.pack()

        # Blank line.
        Label(self, text="").pack()
        Label(self, text="Password").pack()

        # User pass entry.
        user_pass_entry2 = Entry(self, textvariable=user_pass_verify, show="*")
        user_pass_entry2.pack()

        # Login button option.
        login_btn_option = {"text": "Login",
                            "width": "10",
                            "height": "1",
                            }

        empty_space = Label(self, text="")
        empty_space.pack()

        # Login button.
        login_user_button = Button(self, **login_btn_option)
        # Command for button
        login_user_button['command'] = self.login_verify
        # user_pass_entry bind for enter use.
        user_pass_entry2.bind("<Return>", self.login_verify)
        login_user_button.pack()

    # Login verify function for check users.

    def login_verify(self, event=None):
        user_name_v = user_name_verify.get()
        password_v = user_pass_verify.get()
        # Clean entry after press the button.
        user_name_entry1.delete(0, END)
        user_pass_entry2.delete(0, END)

        # Check a database for username and userpass.
        sql = "SELECT * FROM login WHERE BINARY username = '%s'" \
              " AND BINARY userpass = '%s'" % (user_name_v, hashlib.md5(str.encode(password_v)).hexdigest())

        my_cursor.execute(sql)

        pass_success_option = {"text": "Login success",
                               "fg": "green",
                               "font": "Calibri, 12"}

        if my_cursor.fetchone():
            pass_success = Label(self, **pass_success_option)
            pass_success.pack()

            # Open admin screen
            self.open_admin_screen(user_name_v)

        else:
            msg.showwarning(title="Warning", message="Warning user not exist!")

    def open_admin_screen(self, user_name_v):
        window = AdminScreen(self, user_name_v)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()
        self.withdraw()




