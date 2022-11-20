import tkinter as tk
from tkinter import messagebox as msg
import hashlib
from AdminScreen import AdminScreen
from Connection import *

# My cursor.
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
        login_label = tk.Label(self, **login_l_option)
        login_label.pack()

        self.user_name_label_get = tk.StringVar()
        self.user_pass_verify = tk.StringVar()

        # Username label
        tk.Label(self, text="Username").pack()

        # Username entry.
        self.user_name_entry = tk.Entry(self, textvariable=self.user_name_label_get)
        self.user_name_entry.pack()

        # Blank line.
        tk.Label(self, text="").pack()
        tk.Label(self, text="Password").pack()

        # User pass entry.
        self.user_pass_entry = tk.Entry(self, textvariable=self.user_pass_verify, show="*")
        self.user_pass_entry.pack()

        # Login button option.
        login_btn_option = {"text": "Login",
                            "width": "10",
                            "height": "1",
                            }

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Login button.
        login_user_button = tk.Button(self, **login_btn_option)
        # Command for button
        login_user_button['command'] = self.login_verify
        # user_pass_entry bind for enter use.
        self.user_pass_entry.bind("<Return>", self.login_verify)
        login_user_button.pack()

    # Login verify function for check users.
    def login_verify(self, event=None):
        user_name_label_get = self.user_name_label_get.get()
        password_get = self.user_pass_verify.get()
        # Clean entry after press the button.
        self.user_name_entry.delete(0, tk.END)
        self.user_pass_entry.delete(0, tk.END)

        # Check a database for username and userpass.
        sql = "SELECT * FROM login WHERE BINARY username = '%s'" \
              " AND BINARY userpass = '%s'" % (user_name_label_get, hashlib.md5(str.encode(password_get)).hexdigest())

        my_cursor.execute(sql)

        pass_success_option = {"text": "Login success",
                               "fg": "green",
                               "font": "Calibri, 12"}

        if my_cursor.fetchone():
            pass_success = tk.Label(self, **pass_success_option)
            pass_success.pack()

            # Open admin screen
            self.open_admin_screen(user_name_label_get)

        else:
            msg.showwarning(title="Warning", message="Warning user not exist!")

    def open_admin_screen(self, user_name_get):
        window = AdminScreen(self, user_name_get)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()
        self.withdraw()




