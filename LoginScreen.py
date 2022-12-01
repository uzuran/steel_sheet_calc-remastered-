import tkinter as tk
import hashlib

import Config
import Connection
from AdminScreen import AdminScreen


class LoginScreen(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.title("Please login!")
        self.geometry("350x450")

        # Main label.
        login_label = tk.Label(self, Config.login_user_conf())
        login_label.pack()

        self.user_name = tk.StringVar()
        self.user_pass_verify = tk.StringVar()

        # Username label
        tk.Label(self, text="Username").pack()

        # Username entry.
        self.user_name_entry = tk.Entry(self, textvariable=self.user_name)
        self.user_name_entry.pack()

        # Blank line.
        tk.Label(self, text="").pack()
        tk.Label(self, text="Password").pack()

        # User pass entry.
        self.user_pass_entry = tk.Entry(self, textvariable=self.user_pass_verify, show="*")
        self.user_pass_entry.pack()

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Login button.
        login_user_button = tk.Button(self, Config.login_button())
        # Command for button
        login_user_button['command'] = self.login_verify
        # user_pass_entry bind for enter use.
        self.user_pass_entry.bind("<Return>", self.login_verify)
        login_user_button.pack()

    # Login verify function for check users.
    def login_verify(self, event=None):
        user_name_label_get = self.user_name.get()
        password_get = self.user_pass_verify.get()
        # Clean entry after press the button.
        self.user_name_entry.delete(0, tk.END)
        self.user_pass_entry.delete(0, tk.END)

        # Check a database for username and userpass.
        hashed = hashlib.md5(str.encode(password_get)).hexdigest()
        Connection.check_for_user_and_pass(user_name_label_get, hashed)

        if Connection.my_cursor.fetchone():

            # Open admin screen
            self.open_admin_screen(user_name_label_get)

        else:
            Config.warning_msg_user_not_exist()

    def open_admin_screen(self, user_name_get):
        window = AdminScreen(self, user_name_get)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()
        self.withdraw()




