import tkinter as tk
from tkinter import ttk
import Components

import LoginScreen
import OptionScreen
import RegisterUserScreen


class StartPage(tk.Frame):
    def __init__(self, children, controller):
        tk.Frame.__init__(self, children)
        self.controller = controller
        self.put_all()

    def put_all(self):

            # Enter label.
            self.enter_label = tk.Label(self, Components.main_label_conf())
            self.enter_label.pack(Components.option_for_labels())

            self.laser_logo = tk.PhotoImage(file="img/laser.png")
            label_logo = tk.Label(self, image=self.laser_logo)
            label_logo.pack()

            # Setting button.
            self.setting_button = tk.PhotoImage(file="img/settings-icon.png")
            self.button_for_setting = tk.Button(self, image=self.setting_button, borderwidth=0)
            self.button_for_setting.pack(anchor="e", padx=20)
            self.button_for_setting["command"] = lambda: self.controller.show_frame(OptionScreen.OptionPage)

            # Log in button.
            self.log_in_button = tk.Button(self, Components.main_button_conf_login())
            # Command for button
            self.log_in_button['command'] = lambda: self.controller.show_frame(LoginScreen.LoginPage)
            self.log_in_button.pack(Components.option_for_labels())

            # Register button.
            self.register_button = tk.Button(self, Components.main_button_conf_registration())
            # Command for button
            self.register_button['command'] = lambda: self.controller.show_frame(RegisterUserScreen.RegistrationPage)
            self.register_button.pack(Components.option_for_labels())


