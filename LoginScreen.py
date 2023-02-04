import tkinter as tk
import hashlib

import Components
import Connection
from AdminScreen import AdminScreen
import Languages
import StartPage


# second window frame page1
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Main label.
        login_label = tk.Label(self, Components.login_user_conf())
        login_label.pack()

        # Back to main page button.

        self.back_image = tk.PhotoImage(file="img/back.png")
        self.button_image_for_back = tk.Button(self, image=self.back_image, borderwidth=0)
        self.button_image_for_back['command'] = lambda: controller.show_frame(StartPage.StartPage)
        self.button_image_for_back.pack()

        self.user_name_variable = tk.StringVar()
        self.user_pass_variable = tk.StringVar()

        # Username label
        username_label = tk.Label(self, text=Languages.current_lang["username_label"])
        username_label.pack()

        # Username entry.
        self.user_name_login_entry = tk.Entry(self, textvariable=self.user_name_variable)
        self.user_name_login_entry.pack()
        self.user_name_login_entry.focus_set()

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Password label
        self.password_label = tk.Label(self, text=Languages.current_lang["password_label"])
        self.password_label.pack()

        # User pass entry.
        self.user_pass_entry = tk.Entry(self, textvariable=self.user_pass_variable, show="*")
        self.user_pass_entry.pack()

        empty_space = tk.Label(self, text="")
        empty_space.pack()

        # Login button.
        login_user_button = tk.Button(self, Components.login_button())
        # Command for button
        login_user_button['command'] = self.login_verify
        # user_pass_entry bind for enter use.
        self.user_pass_entry.bind("<Return>", self.login_verify)
        login_user_button.pack()

    # Login verify function for check users.
    def login_verify(self, event=None):
        user_name_get = self.user_name_variable.get()
        password_get = self.user_pass_variable.get()
        # Clean entry after press the button.
        self.user_name_login_entry.delete(0, tk.END)
        self.user_pass_entry.delete(0, tk.END)

        # Check a database for username and userpass.
        hashed = hashlib.md5(str.encode(password_get)).hexdigest()
        Connection.check_for_user_and_pass(user_name_get, hashed)

        if Connection.check_for_user_and_pass(user_name_get, hashed):

            # Open admin screen
            self.open_admin_screen(user_name_get)

        else:
            Components.warning_msg_user_not_exist()

    def open_admin_screen(self, user_name_get):
        if not any(isinstance(x, tk.Toplevel) for x in self.winfo_children()):
            AdminScreen(self, user_name_get)





